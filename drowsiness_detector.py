import cv2
import numpy as np
import dlib
import time
from imutils import face_utils
from playsound import playsound
import threading  # Import threading to run the audio in a separate thread

# Initializing the camera and taking the instance
cap = cv2.VideoCapture(0)

# Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Status marking for current state
sleep = 0
drowsy = 0
active = 0

# Set the time limit to 10 minutes (600 seconds)
time_limit = 10   # 1 minutes in seconds change time hereeeeeeeee
start_time = time.time()  # Get the start time

def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    # Checking if it is blinked
    if ratio > 0.25:
        return 2  # Blinked
    elif 0.21 < ratio <= 0.25:
        return 1  # Drowsy
    else:
        return 0  # Active

def play_alert():
    playsound(r"C:\Users\TRUSHA\OneDrive\Desktop\opencvproject\Alarm-2-chosic.com_.mp3")  # Play sound in a new thread

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    face_frame = frame.copy()  # Initialize face_frame

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    if elapsed_time < time_limit:
        # Detected face in faces array
        if len(faces) > 0:
            for face in faces:
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()

                cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                landmarks = predictor(gray, face)
                landmarks = face_utils.shape_to_np(landmarks)

                # The numbers are actually the landmarks which will show eye
                left_blink = blinked(landmarks[36], landmarks[37], 
                                     landmarks[38], landmarks[41], landmarks[40], landmarks[39])
                right_blink = blinked(landmarks[42], landmarks[43], 
                                      landmarks[44], landmarks[47], landmarks[46], landmarks[45])
                
                # Print debug information
                print(f"Left blink: {left_blink}, Right blink: {right_blink}")

                # Now judge what to do for the eye blinks
                if left_blink == 0 or right_blink == 0:
                    sleep += 1

                elif left_blink == 1 or right_blink == 1:
                    drowsy += 1

                else:
                    active += 1

        # Display a generic status during the 10-minute observation period
        cv2.putText(frame, "Monitoring Driver...", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 0), 3)
    else:
        # After 10 minutes, determine the driver's status based on counts
        if sleep > drowsy and sleep > active:
            final_status = "Driver is SLEEPY!"
            color = (255, 0, 0)
            threading.Thread(target=play_alert).start()  # Start the audio in a new thread

        elif drowsy > sleep and drowsy > active:
            final_status = "Driver is DROWSY!"
            color = (0, 0, 255)
            threading.Thread(target=play_alert).start()  # Start the audio in a new thread

        else:
            final_status = "Driver is ACTIVE."
            color = (0, 255, 0)

        # Display the final status
        cv2.putText(frame, final_status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    # Show the frame and results
    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)
    
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break  # Breaks out of the while loop

# Ensure that resources are released when the loop ends
cap.release()
cv2.destroyAllWindows()


