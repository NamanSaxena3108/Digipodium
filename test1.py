import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

last_gesture = None
gesture_start_time = None
delay_seconds = 3 

# Gesture Recognition Logic with unique gestures
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # Open Palm (for starting slideshow)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        index_tip.y < landmarks[6].y and  # Index extended
        middle_tip.y < landmarks[10].y and  # Middle extended
        ring_tip.y < landmarks[14].y and  # Ring extended
        pinky_tip.y < landmarks[18].y):  # Pinky extended
        return "Open Palm"

    # Thumb and Pinky Extended (for adding a new slide)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        pinky_tip.y < landmarks[18].y and  # Pinky extended
        index_tip.y > landmarks[6].y and  # Index bent
        middle_tip.y > landmarks[10].y and  # Middle bent
        ring_tip.y > landmarks[14].y):  # Ring bent
        return "Thumb and Pinky Extended"

    # Index Finger and Thumb Extended (for ending slideshow)
    if (index_tip.y < landmarks[6].y and  # Index extended
        thumb_tip.y < landmarks[3].y and  # Thumb extended
        middle_tip.y > landmarks[10].y and  # Middle bent
        ring_tip.y > landmarks[14].y and  # Ring bent
        pinky_tip.y > landmarks[18].y):  # Pinky bent
        return "Index and Thumb Extended"
    
    # Index Finger Point (for next slide)
    if (index_tip.y < landmarks[6].y and  # Index extended
        middle_tip.y > landmarks[10].y and  # Middle bent
        ring_tip.y > landmarks[14].y and  # Ring bent
        pinky_tip.y > landmarks[18].y and  # Pinky bent
        thumb_tip.y > landmarks[3].y):  # Thumb bent
        return "Index Finger Point"
    
    # Pinky Finger Point (for previous slide)
    if (pinky_tip.y < landmarks[18].y and  # Pinky extended
        index_tip.y > landmarks[6].y and  # Index bent
        middle_tip.y > landmarks[10].y and  # Middle bent
        ring_tip.y > landmarks[14].y and  # Ring bent
        thumb_tip.y > landmarks[3].y):  # Thumb bent
        return "Pinky Finger Point"

    return "Unknown Gesture"

# Map Gesture to PowerPoint Actions
def execute_action(gesture):
    if gesture == "Open Palm":
        pyautogui.press('f5', interval=3)  # Start slideshow
    elif gesture == "Thumb and Pinky Extended":
        pyautogui.hotkey('ctrl', 'm', interval=5)  # Add a new slide
    elif gesture == "Index and Thumb Extended":
        pyautogui.press('esc', interval=5)  # End slideshow
    elif gesture == "Index Finger Point":
        pyautogui.press('right', interval=3)  # Go to the next slide
    elif gesture == "Pinky Finger Point":
        pyautogui.press('left', interval=3)  # Go to the previous slide
    return time.time()

# Start Video Capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame to avoid mirrored actions
    frame = cv2.flip(frame, 1)

    # Convert frame to RGB as required by MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand detection
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gesture = recognize_gesture(hand_landmarks.landmark)
            
            
            h,w,_=frame.shape
            cv2.rectangle(frame, (0,0), (w, 70),  (0,0,0), -1)
            cv2.putText(frame, gesture, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
            last_action_time = execute_action(gesture)

    # Display the resulting frame
    cv2.imshow("Gesture Control for PowerPoint", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()