import cv2
from datetime import datetime
def add_date(frame):
    #do whatever you want here
    cdate=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    h,w,_=frame.shape
    frame=cv2.putText(
        frame,cdate,(20,h-20),
        cv2.FONT_HERSHEY_SIMPLEX,
        .75,(0,155,255),1
    )
    return frame

def read_webcam(idx=0):   
    video=cv2.VideoCapture(idx)    #Read from webcam 
    codec=cv2.VideoWriter_fourcc(*'XVID')
    writer=cv2.VideoWriter('Recorded Video.avi',codec,25,(640,480))
    while True:                         
        state,frame=video.read()        
        if not state:
            break
        #Your logic here
        frame=add_date(frame)
        cv2.imshow('frame',frame)     
        writer.write(frame) 
        if cv2.waitKey(5)== ord('q'): 
            break
    video.release()  
    writer.release()                 
    cv2.destroyAllWindows()            


#Run Logic
if __name__=="__main__":
    read_webcam()