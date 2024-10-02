import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

# Gesture Recognition Logic with unique gestures
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # Thumb and Index Finger Point (for starting slideshow)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        index_tip.y < landmarks[6].y):  # Pinky bent
        return "Thumb and Index Point"

    # Thumb and Middle Finger Point (for adding a new slide)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        middle_tip.y < landmarks[10].y):  # Pinky bent
        return "Thumb and Middle Finger Point"

    # Thumb and Pinky Extended (for adding a new slide)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        pinky_tip.y < landmarks[18].y):  # Ring bent
        return "Thumb and Pinky Extended"

    # Pinky Point (for next slide)
    if (pinky_tip.y < landmarks[18].y):  # Thumb bent
        return "Pinky Point"

    # Ring Finger Point (for previous slide)
    if (ring_tip.y < landmarks[14].y):  # Thumb bent
        return "Ring Finger Point"

    return "Unknown Gesture"

# Map Gesture to PowerPoint Actions
def execute_action(gesture):
    if gesture == "Thumb and Index Point":
        pyautogui.press('f5',interval=3)  # Start slideshow
    elif gesture == "Thumb and Middle Finger Point":
        pyautogui.hotkey('ctrl', 'm',interval=3)  # Add a new slide
    elif gesture == "Thumb and Pinky Extended":
        pyautogui.press('esc',interval=3)  # End slideshow
    elif gesture == "Pinky Point":
        pyautogui.press('right',interval=3)  # Go to the next slide
    elif gesture == "Ring Finger Point":
        pyautogui.press('left',interval=3)  # Go to the previous slide

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

            # Recognize the gesture based on landmarks
            gesture = recognize_gesture(hand_landmarks.landmark)
            if gesture != "Unknown Gesture":
                # Execute the action for the gesture
                execute_action(gesture)

            # Display recognized gesture on screen
            cv2.putText(frame, gesture, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow("Gesture Control for PowerPoint", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
