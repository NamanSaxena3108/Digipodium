import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Create a blank image to draw on
drawing_image = np.zeros((480, 640, 3), dtype="uint8")

# Variables to track the drawing state
is_drawing = False
previous_x, previous_y = None, None

# Start Video Capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame to avoid mirrored drawing
    frame = cv2.flip(frame, 1)

    # Convert frame to RGB as required by MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand detection
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of the index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[8]

            # Convert normalized coordinates to pixel coordinates
            height, width, _ = frame.shape
            index_x = int(index_finger_tip.x * width)
            index_y = int(index_finger_tip.y * height)

            # Check if drawing mode is active (e.g., when the index finger is near the thumb)
            thumb_tip = hand_landmarks.landmark[4]
            thumb_x = int(thumb_tip.x * width)
            thumb_y = int(thumb_tip.y * height)

            # If thumb and index finger are close, we start drawing
            if abs(index_x - thumb_x) < 30 and abs(index_y - thumb_y) < 30:
                is_drawing = True
            else:
                is_drawing = False
                previous_x, previous_y = None, None

            # Draw line if drawing mode is active
            if is_drawing:
                if previous_x is not None and previous_y is not None:
                    # Draw a line from the previous index position to the current one
                    cv2.line(drawing_image, (previous_x, previous_y), (index_x, index_y), (0, 255, 0), 5)
                previous_x, previous_y = index_x, index_y

    # Overlay the drawing on the frame
    frame = cv2.add(frame, drawing_image)

    # Display the resulting frame
    cv2.imshow("Hand Drawing", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
