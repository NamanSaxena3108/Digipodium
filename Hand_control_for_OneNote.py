import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

drawing_mode = False  # Flag to toggle drawing mode

# Gesture Recognition Logic with unique gestures
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # Thumb and Index Finger Point (for selecting pen 1)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        index_tip.y < landmarks[6].y and  # Index extended
        middle_tip.y > landmarks[10].y and  # Middle finger bent
        ring_tip.y > landmarks[14].y and  # Ring finger bent
        pinky_tip.y > landmarks[18].y):  # Pinky bent
        return "Thumb and Index Point"

    # Thumb and Pinky Spread (for selecting pen 2)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        index_tip.y > landmarks[6].y and  # Index bent
        middle_tip.y > landmarks[10].y and  # Middle finger bent
        ring_tip.y > landmarks[14].y and  # Ring finger bent
        pinky_tip.y < landmarks[18].y):  # Pinky extended
        return "Thumb and Pinky Spread"

    # Three Finger Pinch (for undo)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        abs(thumb_tip.x - index_tip.x) < 0.05 and  # Thumb and index are close
        middle_tip.y < landmarks[10].y and  # Middle finger extended
        ring_tip.y > landmarks[14].y and  # Ring bent
        pinky_tip.y > landmarks[18].y):  # Pinky bent
        return "Three Finger Pinch"

    # Index Finger Point (for drawing)
    if (index_tip.y < landmarks[6].y and  # Index finger extended
        middle_tip.y > landmarks[10].y and  # Middle finger bent
        ring_tip.y > landmarks[14].y and  # Ring finger bent
        pinky_tip.y > landmarks[18].y):  # Pinky finger bent
        return "Index Finger Point"


    # Three Finger Spread (for selecting the eraser)
    if (thumb_tip.y < landmarks[3].y and  # Thumb extended
        index_tip.y < landmarks[6].y and  # Index extended
        middle_tip.y < landmarks[10].y and  # Middle extended
        ring_tip.y > landmarks[14].y and  # Ring bent
        pinky_tip.y > landmarks[18].y):  # Pinky bent
        return "Three Finger Spread"

    # Pinky Point (for next page)
    if (pinky_tip.y < landmarks[18].y and  # Pinky extended
        ring_tip.y > landmarks[14].y and  # Ring bent
        middle_tip.y > landmarks[10].y and  # Middle bent
        index_tip.y > landmarks[6].y and  # Index bent
        thumb_tip.y > landmarks[3].y):  # Thumb bent
        return "Pinky Point"

    # Ring Finger Point (for previous page)
    if (ring_tip.y < landmarks[14].y and  # Ring extended
        pinky_tip.y > landmarks[18].y and  # Pinky bent
        middle_tip.y > landmarks[10].y and  # Middle bent
        index_tip.y > landmarks[6].y and  # Index bent
        thumb_tip.y > landmarks[3].y):  # Thumb bent
        return "Ring Finger Point"

    return "Unknown Gesture"

# Map Gesture to OneNote Actions
def execute_action(gesture):
    global drawing_mode

    if gesture == "Thumb and Index Point":
        pyautogui.hotkey('ctrl', '1')  # Select first pen
    elif gesture == "Thumb and Pinky Spread":
        pyautogui.hotkey('ctrl', '2')  # Select second pen
    elif gesture == "Three Finger Pinch":
        pyautogui.hotkey('ctrl', 'z')  # Undo the last action
    elif gesture == "Index Finger Point":
        if drawing_mode:
            pyautogui.mouseDown()  # Start drawing
        else:
            pyautogui.mouseUp()  # Stop drawing
    elif gesture == "Three Finger Spread":
        pyautogui.hotkey('ctrl', 'n')  # Select eraser
    elif gesture == "Pinky Point":
        pyautogui.hotkey('ctrl', 'pagedown')  # Navigate to the next page
    elif gesture == "Ring Finger Point":
        pyautogui.hotkey('ctrl', 'pageup')  # Navigate to the previous page

# Start Video Captureq
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
                # If drawing mode is enabled, draw with the pen
                if drawing_mode:
                    x, y = int(hand_landmarks.landmark[8].x * frame.shape[1]), int(hand_landmarks.landmark[8].y * frame.shape[0])
                    pyautogui.moveTo(x, y)
                    execute_action(gesture)
                else:
                    # Execute the action for the gesture
                    execute_action(gesture)

            # Display recognized gesture on screen
            cv2.putText(frame, gesture, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow("Gesture Control for OneNote", frame)

    # Toggle drawing mode with 'd'
    if cv2.waitKey(1) & 0xFF == ord('d'):
        drawing_mode = not drawing_mode

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
