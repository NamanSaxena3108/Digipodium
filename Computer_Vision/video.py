import cv2

def process_something(frame):
    #do whatever you want here
    return frame

def read_video(path):
    # Read the video from the specified path 
    video=cv2.VideoCapture(path)        #Read from video
    while True:                         #infinite loop
        state,frame=video.read()        #State:Whether data is present or not / Frame: check for actual frame from video
        if not state:
            break
        #Your logic here
        frame=process_something(frame)
        cv2.imshow('frame',frame)      #Display the image or frame
        if cv2.waitKey(5)== ord('q'):  #if pressed on q on keyboard then quit / in this 10 is the speed of the video playing
            break
    video.release()                    #Free the video from memory
    cv2.destroyAllWindows()            #close the window


#Run Logic
if __name__=="__main__":
    read_video(r"C:\Users\Naman\OneDrive\Videos\Captures\7624761-hd_1920_1080_30fps.mp4")