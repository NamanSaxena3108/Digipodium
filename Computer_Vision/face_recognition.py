import cv2
import mediapipe as mp

mp_face_detection=mp.solutions.face_detection
mp_drawing=mp.solutions.drawing_utils

def process_image(frame,detections):
    #color Converstion
    frame.flags.writeable=False
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=detections.process(frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    frame.flags.writeable=True
    if result.detections:
        for output in result.detections:
            mp_drawing.draw_detection(frame,output)
    return frame

def read_webcam(idx=0):   
    with mp_face_detection.FaceDetection() as detection:
        video=cv2.VideoCapture(idx)        
        while True:                         
            state,frame=video.read()        
            if not state:
                break
            #Your logic here
            frame=process_image(frame,detection)
            cv2.imshow('frame',frame)      
            if cv2.waitKey(5)== ord('q'): 
                break
        video.release()                    
    cv2.destroyAllWindows()            


    #Run Logic
if __name__=="__main__":
    read_webcam()