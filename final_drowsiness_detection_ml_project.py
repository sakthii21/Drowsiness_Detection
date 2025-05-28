import cv2
import numpy as np
from scipy.spatial import distance

# Function to calculate Eye Aspect Ratio (EAR)
def calculate_EAR(eye_points):
    if len(eye_points) < 6:
        return 0  # If not enough points are available to calculate EAR, return 0
    # Calculate the EAR based on the 6 points for each eye (use indexes correctly)
    A = distance.euclidean(eye_points[1], eye_points[5])  # Vertical distance (top to bottom)
    B = distance.euclidean(eye_points[2], eye_points[4])  # Vertical distance (middle to bottom)
    C = distance.euclidean(eye_points[0], eye_points[3])  # Horizontal distance (left to right)
    ear = (A + B) / (2.0 * C)
    return ear

# Load OpenCV Haar Cascade for face detection and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Check if the frame was captured successfully
    if not _:
        print("Error: Unable to capture frame")
        break

    # Convert the frame to grayscale (OpenCV face detector works on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    no_danger_flag = False  # Initialize the flag for "NO DANGER" detection

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Region of interest (ROI) for eyes within the face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)

        eye_landmarks = []

        # If eyes are detected, calculate EAR for each eye
        if len(eyes) > 0:
            for (ex, ey, ew, eh) in eyes:
                # Approximate the coordinates for the top, bottom, left, and right corners of the eyes
                eye_landmarks.append([(ex, ey), (ex + ew, ey), (ex + ew, ey + eh), (ex, ey + eh)])

            if len(eye_landmarks) == 2:
                leftEye = eye_landmarks[0]
                rightEye = eye_landmarks[1]

                # Calculate EAR for both eyes (using corners of the eyes)
                EAR_left = calculate_EAR([leftEye[0], leftEye[1], leftEye[2], leftEye[3]])  # EAR for left eye
                EAR_right = calculate_EAR([rightEye[0], rightEye[1], rightEye[2], rightEye[3]])  # EAR for right eye
                EAR = (EAR_left + EAR_right) / 2  # Average EAR

                # If EAR is below the threshold, consider it as drowsy (eyes closed)
                if EAR < 0.80:  # Adjust EAR threshold for detecting open eyes
                    cv2.putText(frame, "NO DANGER", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 4)  # Red text
                    print("DANGER - Eyes closed")  # Print message for drowsy state (eyes closed)
                    no_danger_flag = True  # Set the flag to True
                else:
                    cv2.putText(frame, "DANGER", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 4)  # Green text
                    print("No Danger")  # Print EAR value when no danger

                # Print EAR for debugging purposes
                print(f"EAR: {EAR}")

    # If "NO DANGER" was not detected, display "DANGER"
    if not no_danger_flag:
        cv2.putText(frame, "DANGER", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)  # Red text
        print("DANGER - No eyes detected or other danger condition")

    # Show the frame with results
    cv2.imshow("Drowsiness Detection", frame)

    # Press 'Esc' key to exit the loop
    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII value for 'Esc'
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
