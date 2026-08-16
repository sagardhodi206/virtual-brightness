import cv2
import mediapipe as mp
import numpy as np
import math
import screen_brightness_control as sbc

# -------------------------------------------------------------
# 1. INITIALIZE MEDIAPIPE HANDS
# -------------------------------------------------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Initialize Screen Brightness UI variables
bright_bar = 400
bright_per = 0

# Open Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Mirror the frame horizontally for natural gesture movement
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert BGR frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmark skeleton on hand
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Extract Index Finger Tip (Landmark 8) and Thumb Tip (Landmark 4)
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]

            # Convert normalized landmarks to pixel coordinates
            ix, iy = int(index_tip.x * w), int(index_tip.y * h)
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
            cx, cy = (ix + tx) // 2, (iy + ty) // 2  # Midpoint coordinate

            # Draw circles and line connecting thumb and index finger
            cv2.circle(frame, (ix, iy), 10, (0, 255, 255), cv2.FILLED)
            cv2.circle(frame, (tx, ty), 10, (0, 255, 255), cv2.FILLED)
            cv2.line(frame, (ix, iy), (tx, ty), (0, 255, 255), 3)
            cv2.circle(frame, (cx, cy), 8, (0, 255, 255), cv2.FILLED)

            # Calculate Euclidean distance between fingers
            distance = math.hypot(ix - tx, iy - ty)

            # -------------------------------------------------------------
            # 2. MAP DISTANCE TO BRIGHTNESS LEVEL
            # -------------------------------------------------------------
            # Distance range: approx 20px (close) to 200px (extended)
            # Map distance to percentage (0% - 100%)
            bright_per = np.interp(distance, [20, 200], [0, 100])
            
            # Map distance to UI bar height (y-coordinates: 400 = 0%, 150 = 100%)
            bright_bar = np.interp(distance, [20, 200], [400, 150])

            # Apply brightness level to laptop display
            try:
                sbc.set_brightness(int(bright_per))
            except Exception as e:
                pass  # Handles hardware driver quirks gracefully

            # Visual indicator: turns yellow when brightness hits minimum
            if distance < 20:
                cv2.circle(frame, (cx, cy), 10, (0, 200, 255), cv2.FILLED)

    # -------------------------------------------------------------
    # 3. DRAW ON-SCREEN BRIGHTNESS UI
    # -------------------------------------------------------------
    # Outer bar frame
    cv2.rectangle(frame, (50, 150), (85, 400), (255, 255, 255), 2)
    # Inner dynamic level bar
    cv2.rectangle(frame, (50, int(bright_bar)), (85, 400), (0, 255, 255), cv2.FILLED)
    # Percentage readout
    cv2.putText(frame, f'{int(bright_per)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    # Show live feed
    cv2.imshow("Virtual Brightness Control", frame)

    # Press 'q' to quit application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()