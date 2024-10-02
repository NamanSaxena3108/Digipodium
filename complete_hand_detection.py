import cv2
import mediapipe as mp
import math
import numpy as np

    


mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


video=cv2.VideoCapture(0)
with mp_hands.Hands() as detection:
    while True:
        state,frame=video.read()
        if not state:
            break
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=detection.process(frame)
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        l=[]
        if results.multi_hand_landmarks:
            myHand=results.multi_hand_landmarks[0]
            for id,lm in enumerate(myHand.landmark):
                h,w,c=frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                l.append([id,cx,cy])
                print(cx, cy)
        if len(l) != 0:
            x1,y1=l[4][1],l[4][2]
            x2,y2=l[8][1],l[8][2]
            x3,y3=l[12][1],l[12][2] 
            x4,y4=l[16][1],l[16][2] 
            x5,y5=l[20][1],l[20][2] 

            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1)**2)

            cv2.circle(frame,(x1,y1),10,(255,255,255))
            cv2.circle(frame,(x2,y2),10,(255,255,255))
            cv2.circle(frame,(x3,y3),10,(255,255,255))
            cv2.circle(frame,(x4,y4),10,(255,255,255))
            cv2.circle(frame,(x5,y5),10,(255,255,255))

            cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2)
            cv2.line(frame,(x2,y2),(x3,y3),(255,0,0),2)
            cv2.line(frame,(x3,y3),(x4,y4),(255,0,0),2)
            cv2.line(frame,(x4,y4),(x5,y5),(255,0,0),2)

            length=math.hypot(x2-x1,y2-y1)
            if length<20:
                cv2.line(frame,(x1,y1),(x2,y2),(255,255,0),2)
        cv2.imshow('hand',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
video.release()
