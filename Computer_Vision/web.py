import cv2

def process_something(frame):
    #do whatever you want here
    return frame

def read_webcam(idx=0):   
    video=cv2.VideoCapture(idx)        #Read from webcam 
    while True:                         
        state,frame=video.read()        
        if not state:
            break
        #Your logic here
        frame=process_something(frame)
        cv2.imshow('frame',frame)      
        if cv2.waitKey(5)== ord('q'): 
            break
    video.release()                    
    cv2.destroyAllWindows()            


#Run Logic
if __name__=="__main__":
    read_webcam()