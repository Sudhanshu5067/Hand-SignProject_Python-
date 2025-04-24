import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

def get_hand_sign_message(finger_count):
    messages = {
        0: "Closed Fist",
        1: "I am Happy",
        2: "Smiling",
        3: "I am feeling boring",
        4: "Four Fingers",
        5: "Open Hand",
        6: "I am good",
        7: "lack of Seekness",
        8: "Smiling is good for healrh",
        9: "I am feeling boring",
        10: "Four Fingers equals"
    }
    return messages.get(finger_count, "Unknown Sign")

def count_fingers_single_hand(hand_landmarks):
    # Get finger tip and pip landmarks
    finger_tips = [8, 12, 16, 20]  # Index, middle, ring, pinky tips
    thumb_tip = 4
    
    fingers = []
    
    # Check thumb (comparing with thumb base)
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    
    # Check other fingers
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    
    return sum(fingers)

while True:
    success, img = cap.read()
    if not success:
        break
        
    # Flip the image horizontally for a later selfie-view display
    img = cv2.flip(img, 1)
    
    # Convert the BGR image to RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process the image and detect hands
    results = hands.process(rgb_img)
    
    # Variables to store total finger count
    total_fingers = 0
    
    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count fingers for this hand
            hand_fingers = count_fingers_single_hand(hand_landmarks)
            total_fingers += hand_fingers
            
        # Get hand sign message
        hand_sign = get_hand_sign_message(total_fingers)
        
        # Display total finger count and hand sign
        cv2.putText(img, f'Total Fingers: {total_fingers}', (50, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(img, f'Sign: {hand_sign}', (50, 100), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the image
    cv2.imshow('Hand Sign Recognition', img)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows() 