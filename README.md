# 🛑 DrowsyDrive-Detector

A real-time Python-based system that detects whether a driver is **Active**, **Drowsy**, or **Sleepy** using eye-blink detection via facial landmarks.  
This project promotes road safety by identifying early signs of fatigue during driving.

---

## 🎯 Objective

To monitor the driver's alertness over a 10-minute period using webcam-based eye-blink tracking.  
If the driver is found to be **Drowsy** or **Sleepy**, an alert sound is played to regain their attention.

---

## 📌 Features

- Real-time webcam feed using **OpenCV**
- Face and eye detection using **dlib** with `shape_predictor_68_face_landmarks.dat`
- Classifies the driver as:
  - 🟢 **Active**
  - 🟡 **Drowsy**
  - 🔴 **Sleepy**
- Plays an alarm sound if the driver shows fatigue
- Automatically evaluates the final driver status after 10 minutes

---

## 🛠️ Tech Stack

| Category              | Tools Used                                 |
|-----------------------|---------------------------------------------|
| Programming Language  | Python                                      |
| Libraries             | OpenCV, dlib, imutils, numpy, playsound     |
| Environment           | Local system with camera access             |

---

## 🗂️ File Structure

DrowsyDrive-Detector/  
│  
├── drowsiness_detector.py              # Main Python script  
├── Alarm-2-chosic.com_.mp3             # Alarm sound file  
├── shape_predictor_68_face_landmarks.dat  # Pre-trained facial landmark model  
├── requirements.txt                    # List of dependencies  
└── README.md                           # Project documentation  

---

