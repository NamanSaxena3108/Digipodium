#refer to mediapipe/docs/solutions/hands.md for more in github
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def process_image(frame,detections):
    #color Converstion
    frame.flags.writeable=False
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=detections.process(frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    frame.flags.writeable=True
    if result.multi_hand_landmarks:
      for hand_landmarks in result.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    return frame

def read_webcam(idx=0):   
    with mp_hands.Hands() as detection:
        video=cv2.VideoCapture(idx)        
        while True:                         
            state,frame=video.read()        
            if not state:
                break
            #Your logic here
            frame=process_image(frame,detection)
            cv2.imshow('frame',frame)      
            if cv2.waitKey(1)== ord('q'): 
                break
        video.release()                    
    cv2.destroyAllWindows()            


    #Run Logic
if __name__=="__main__":
    read_webcam()
