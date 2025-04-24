# Hill Climb Racing Hand Gesture Control

This project allows you to control Hill Climb Racing using hand gestures captured through your webcam. It uses computer vision to detect hand gestures and translates them into game controls.

## Features

- **Real-time hand detection**: Uses MediaPipe to track your hand in real-time
- **Gesture-based controls**:
  - Open hand (5 fingers) = Throttle (right arrow)
  - Closed fist (0 fingers) = Brake (left arrow)
  - Thumb only = Lean forward (up arrow)
  - Index finger only = Lean backward (down arrow)
  - Thumb+Index pinch = Alternative throttle
- **Visual feedback**:
  - Hand detection box around your hand
  - Control indicator showing the current active control
  - Separate window showing the cropped hand image with gesture visualization
  - Color-coded gesture indicators

## Requirements

- Python 3.7 or higher
- Webcam
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone this repository or download the files
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the control script:
```bash
python hill_climb_racing_control.py
```

2. Switch to the Hill Climb Racing game window when prompted (you have 5 seconds)

3. Use the following hand gestures to control the game:
   - Open your hand (all fingers extended) to accelerate
   - Close your fist to brake
   - Show only your thumb to lean forward
   - Show only your index finger to lean backward
   - Pinch your thumb and index finger together as an alternative way to throttle

4. The program will display:
   - A green box around your detected hand
   - The current control being activated above your hand
   - A separate window showing the cropped hand image with gesture visualization

5. Press 'q' to quit the program

## How it works

- **Hand Detection**: MediaPipe is used to detect hand landmarks in real-time
- **Gesture Recognition**: The system analyzes finger positions to determine which gesture is being made
- **Gesture Smoothing**: A history-based smoothing algorithm reduces jitter and false detections
- **Game Control**: PyAutoGUI simulates keyboard inputs based on the detected gestures
- **Visual Feedback**: OpenCV is used to display real-time visual feedback

## Troubleshooting

- **Lag issues**: If you experience lag, try closing other applications to free up system resources
- **Detection issues**: Ensure good lighting and a clear view of your hand
- **Control issues**: Make sure your hand gestures are clear and distinct

## License

This project is open source and available under the MIT License. 