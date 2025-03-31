<h1 align="left">Smart Crib For Infants</h1>

###

<h2 align="left">📌 Project Description</h2>

###

<p align="left">Smart Crib for Infants is an intelligent crib that utilizes AI and sensors to monitor the baby and respond automatically when they cry. The system analyzes sounds, sends notifications, and activates music or rocks the crib to soothe the baby.</p>

###

<h2 align="left">🎯 Project Goals</h2>

###

<p align="left">✅ Real-time baby monitoring using a live-streaming camera.<br>✅ Sound analysis to determine the reason for crying and send alerts to parents.<br>✅ Automatic soothing through crib rocking, music playback, and toy activation.<br>✅ A mobile application for parents to control crib functions.</p>

###

<h2 align="left">🛠️ Technologies Used</h2>

###

<p align="left"><h3 align="left">🔹Hardware</h3>Raspberry Pi (as the main controller).<br><br>Microphone to capture baby sounds.<br><br>Camera for live streaming.<br><br>DHT sensor to measure temperature and humidity.<br><br>Vibration motors to rock the crib.<br><br>Speakers to play music.<br><br>Moving toys to grab the baby’s attention.<br><br><h3 align="left">🔹Software</h3>Flutter for mobile app development.<br><br>Firebase for data storage and notifications.<br><br>Python for AI-based sound analysis.<br><br>Flask Server to handle communication between Raspberry Pi and the app.</p>


![image](https://github.com/user-attachments/assets/37fb615b-14d7-4f6a-845b-04486ef5129b)


###

<h2 align="left">🔍 How the Smart Crib Works</h2>

###

<p align="left"><h3 align="left">1- Data Capture:</h3>Microphone captures the baby’s cries.<br><br>DHT sensor measures crib temperature and humidity.<br><br>Camera provides a live video stream for monitoring.<br><br><h3 align="left">2- Data Analysis:</h3>Data is sent to the Raspberry Pi, which checks the baby’s condition.<br><br>If the baby is crying, the sound data is sent to a server for AI analysis.<br><br><h3 align="left">3- Response Processing:</h3>The results are sent to Firebase, enabling the app to display notifications and updates.<br><br>Parents can watch the live stream and check the baby’s status via the app.<br><br>In manual mode, parents can control music, toys, or crib rocking through the app.<br><br><h3 align="left">4- Automatic Response:</h3>If the system is in automatic mode, the crib will react based on sound analysis, such as:<br>✅ Playing music to soothe the baby.<br>✅ Activating toys to grab the baby’s attention.<br>✅ Rocking the crib to help the baby sleep.</p>


![image](https://github.com/user-attachments/assets/678336fd-804d-4237-9293-7c7a753db81d)


###

<h2 align="left">AI Models</h2>

###

<p align="left">If you are interested in AI models, you can check out these repositories:</p>

###

<p align="left">✅ https://github.com/Mohammad-Shaikh-Ibrahim/CrySense<br>✅ https://github.com/Mohammad-Shaikh-Ibrahim/babycry<br>✅ https://github.com/Mohammad-Shaikh-Ibrahim/baby_cry_detection</p>

###

<h3 align="left">Cry detection model</h3>

###

<p align="left">We built a model to recognize and analyze sounds that can distinguish crying from other sounds, then trained it on 80%, epochs =50 and tested it on 20% The accuracy we got was 97.7%</p>

###

<p align="left">The Model: https://www.kaggle.com/models/mohammadalshaikh00/cry-detection-model</p>

###

<p align="left">Dataset: https://www.kaggle.com/datasets/mohammadalshaikh00/cry-detection-dataset</p>

###

![image](https://github.com/user-attachments/assets/7f466796-3c11-4f19-9274-a3f903918a0b)

###

<h3 align="left">Cry reasons detection model</h3>

###

<p align="left">We built a model to recognize and analyze crying causes so that it could distinguish between each crying sound and classify it into one of the nine causes mentioned, then we trained it on 80%, epochs =50 , and tested it on 20%  <br>The accuracy we obtained was 87.16%</p>

###

<p align="left">The Model: https://www.kaggle.com/models/mohammadalshaikh00/cry-reasons-detection-model</p>

###

<p align="left">Dataset: https://www.kaggle.com/datasets/mohammadalshaikh00/cry-reasons-detection-dataset</p>

###

![image](https://github.com/user-attachments/assets/042f0cf0-37b1-4bbd-b2c8-4d87fd107191)

###
###
###
