# 🛑 DrowsyDrive-Detector

A real-time Python-based system that detects whether a driver is **active**, **drowsy**, or **sleepy** using eye blink detection via facial landmarks. This project helps promote road safety by identifying signs of fatigue during driving.

---

## 🎯 Objective

To monitor the driver's alertness over a 10-minute period using webcam-based eye-blink tracking. If the driver is found to be **drowsy** or **sleepy**, an alert sound is played to grab their attention.

---

## 📌 Features

- Real-time webcam feed using OpenCV
- Face and eye detection using `dlib` and `shape_predictor_68_face_landmarks.dat`
- Classifies the driver as:
  - **Active**
  - **Drowsy**
  - **Sleepy**
- Plays an alarm sound if the driver is not attentive
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

