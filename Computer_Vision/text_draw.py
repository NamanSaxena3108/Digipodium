import cv2

def add_text(frame):
    #do whatever you want here
    text="Hey this side Naman"
    fs=1  #scale of font
    font=cv2.FONT_HERSHEY_SIMPLEX
    color=(0,0,255) #Red Color
    thickness=1
    origin=(50,50)
    frame=cv2.putText(frame,text,origin,font,fs,color,thickness)

    #direct value passing in putText
    cv2.putText(frame,"This is INTRO to Data Science with OpenCV",(50,75),font,.5,color,2)
    return frame

def read_webcam(idx=0):   
    video=cv2.VideoCapture(idx)        #Read from webcam 
    while True:                         
        state,frame=video.read()        
        if not state:
            break
        #Your logic here
        frame=add_text(frame)
        cv2.imshow('frame',frame)      
        if cv2.waitKey(5)== ord('q'): 
            break
    video.release()                    
    cv2.destroyAllWindows()            


#Run Logic
if __name__=="__main__":
    read_webcam()