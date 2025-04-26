**Description :**

A real-time hand sign recognition system built with Python, OpenCV, and MediaPipe.

Detects hand landmarks and counts the number of raised fingers.

Displays a specific message based on the detected number of fingers.

Provides real-time feedback with visual hand landmarks.

Simple, lightweight, and works directly with a webcam.

**🛠️ Technologies Used**
Python 3.x

OpenCV (for image capture and processing)

MediaPipe (for hand tracking and landmark detection)

NumPy (for numerical operations)

**🚀 Installation and Setup**
**Clone the repository**

bash
Copy
Edit
git clone https://github.com/your-username/hand-sign-recognition.git
cd hand-sign-recognition
Install required packages

bash
Copy
Edit
pip install opencv-python mediapipe numpy
**Run the project**

bash
Copy
Edit
python hand_sign_recognition.py
**🎯 How It Works**
The webcam captures live video frames.

Each frame is processed to detect hand landmarks.

Finger positions are analyzed to determine how many fingers are raised.

A predefined message is displayed based on the total number of fingers detected.

Landmarks are drawn on the screen for better visualization.

Press 'q' at any time to exit the application.
