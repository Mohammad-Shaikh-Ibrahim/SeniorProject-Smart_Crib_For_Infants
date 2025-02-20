#to activate the venv: source .venv/bin/activate
#python app3.py
import cv2
import requests
import threading
import pyaudio
import RPi.GPIO as GPIO
import time
import subprocess
import Adafruit_DHT
import firebase_admin
from firebase_admin import credentials, db

# GPIO setup
servo_pin = 18
dc_motor_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(dc_motor_pin, GPIO.OUT)

servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(0)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 21

# Firebase setup
cred = credentials.Certificate("smart-baby-nest-firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-baby-nest-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Firebase reference
firebase_ref = db.reference()

# Flags
stop_sending_sensor_data = False

# Function to check Firebase for manual control
def check_firebase_control():
    global stop_sending_sensor_data
    while True:
        control_status = firebase_ref.child('Manual_control_status').get()
        if control_status:
            print("Manual control enabled.")
            perform_actions()
        time.sleep(2)

# Function to stream video
def stream_video():
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to access camera")
                continue
            _, buffer = cv2.imencode('.jpg', frame)

            try:
                response = requests.post(
                    "http://192.168.1.12:5000/upload_frame", 
                    files={"frame": buffer.tobytes()},
                    timeout=20
                )
                if response.status_code == 200:
                    response_data = response.json()
                    if response_data.get("child_detected"):
                        print("Child detected, starting audio analysis...")
                        if result_audio():
                            firebase_ref.update({
								"crying_status": True,
								"Manual_control_status":True
								})
                            perform_actions()
                else:
                    print(f"Error: Received invalid status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error in stream_video: {e}")
            time.sleep(0.1)
    finally:
        cap.release()

# Function to analyze audio and check if the baby is crying
def result_audio():
    try:
        response = requests.post("http://192.168.1.12:5001/analyze_audio", timeout=20)
        print("Audio analysis in progress...")
        if response.status_code == 200:
            print(f"Server response: {response.json()}")
            return response.json().get("Crying") == "yes"
        else:
            print(f"Error: Received status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error in result_audio: {e}")
        return False

# Function to execute actions when the baby is crying or manual control is enabled
def perform_actions():
    global stop_sending_sensor_data
    stop_sending_sensor_data = True

    # تحديث Manual_control_status و crying_status إلى True
    firebase_ref.update({
        "Manual_control_status":True
    })

    print("Starting actions: Music, Motor, and Crib Movement for 60 seconds.")
    start_time = time.time()
    music_process = subprocess.Popen(["mpg321", "0117.MP3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        while time.time() - start_time < 45:
            # تحريك السرير
            servo_pwm.ChangeDutyCycle(7)  
            time.sleep(1)
            servo_pwm.ChangeDutyCycle(0)

            # تشغيل محرك DC
            GPIO.output(dc_motor_pin, GPIO.HIGH)
            time.sleep(1)

        # إيقاف كل شيء بعد 60 ثانية
        GPIO.output(dc_motor_pin, GPIO.LOW)
        music_process.terminate()  # إيقاف الموسيقى
        print("Actions stopped after 60 seconds.")

    except Exception as e:
        print(f"Error in perform_actions: {e}")

    finally:
        # إعادة Manual_control_status و crying_status إلى False بعد انتهاء العمل
        firebase_ref.update({
            "Manual_control_status": False
        })
        stop_sending_sensor_data = False


# Function to read sensor data and send it to the server
def read_and_send_sensor_data():
    global stop_sending_sensor_data
    while True:
        if stop_sending_sensor_data:
            time.sleep(2)
            continue

        try:
            humidity, temperature = Adafruit_DHT.read(Adafruit_DHT.DHT11, 21)
            if humidity is not None and temperature is not None:
                data = {"temperature": temperature, "humidity": humidity}
                try:
                    response = requests.post("http://192.168.1.12:5050/upload_sensor_data", json=data, timeout=5)
                    if response.status_code != 200:
                        print(f"Error: Failed to send sensor data, status code {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Error in sending sensor data: {e}")
            time.sleep(60)
        except Exception as e:
            print(f"Error in read_and_send_sensor_data: {e}")

# Start threads
video_thread = threading.Thread(target=stream_video)
sensor_thread = threading.Thread(target=read_and_send_sensor_data)
firebase_control_thread = threading.Thread(target=check_firebase_control)

video_thread.start()
sensor_thread.start()
firebase_control_thread.start()

try:
    video_thread.join()
    sensor_thread.join()
    firebase_control_thread.join()
finally:
    GPIO.cleanup()
