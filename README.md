# Drowsiness_Detection

# 🛑 Real-Time Drowsiness Detection using OpenCV

A simple yet powerful **Drowsiness Detection System** that uses Haar Cascades and Eye Aspect Ratio (EAR) to monitor eye closure in real-time and detect signs of drowsiness.

---

## 🧠 Overview

Driver fatigue is a major cause of road accidents worldwide. This system aims to prevent such incidents by analyzing live webcam feed to:
- Detect faces and eyes using Haar cascades
- Calculate the Eye Aspect Ratio (EAR)
- Alert when the eyes remain closed for a prolonged period (indicating drowsiness)

---

## 📸 Demo

![image](https://github.com/user-attachments/assets/cee6327e-ed54-427a-8670-5b4ba0d0ac85)

---

## ⚙️ Tech Stack

- **Python**
- **OpenCV**
- **NumPy**
- **SciPy** (`scipy.spatial.distance` for EAR)
- Haar Cascade Classifiers (pre-trained)

---

## 🔍 How It Works

- **Face & Eye Detection:** Uses OpenCV's Haar cascades to locate faces and eyes in real-time.
- **EAR Calculation:** Eye Aspect Ratio is calculated based on detected eye landmarks.
- **Alert Logic:** If the average EAR falls below a set threshold (`< 0.80`) for both eyes, it's flagged as drowsy and the system displays `"DANGER"`

---

## 📦 Installation

1. **Clone this repo**
   ```bash
   git clone https://github.com/sakthii21/Drowsiness-Detection.git
   cd Drowsiness-Detection
---

**Install required packages**

pip install opencv-python numpy scipy
---

**Run the project**

python detect_drowsiness.py

---

**EAR Formula**

The Eye Aspect Ratio (EAR) is a mathematical formula that estimates eye openness:

**EAR = (||p2 − p6|| + ||p3 − p5||) / (2 * ||p1 − p4||)**

If the eyes are closing, vertical distances shrink → EAR drops.
---

⚠️ Known Limitations
- Uses rectangle-based eye approximation (not precise landmarks)

- False positives in low light or if face partially visible

EAR threshold may need calibration for different faces
---

🚀 Improvements You Can Add

- Use dlib or mediapipe for better landmark detection

- Add sound alert (pygame or playsound)

- Record alert logs for monitoring

Package with a GUI (e.g., Tkinter or PyQt)
---

🪪 License
MIT License. Use freely, but give credit 😊
---

🙌 Acknowledgments
- OpenCV Haar cascades

- SciPy for EAR calculation

Stay awake. Stay safe. 🚗💤


---

Let me know if you'd like to generate a logo or preview images for this project, or add badges (like Python version, OpenCV version, etc.).







