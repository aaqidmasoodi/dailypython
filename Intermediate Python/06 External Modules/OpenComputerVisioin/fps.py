# how to calculate actual frame per second being processeed
# 60fps 35fps

# google ml model

import cv2 as cv
import time

capture = cv.VideoCapture('face.mp4')

# stop watch you can get the current time at moment 
# you can get the current time in milliseconds

c_time = 0
p_time = 0


while True:

 ret, frame = capture.read() # reading a new frame time

 frame = cv.resize(frame, (frame.shape[1]//3, frame.shape[0]//3), interpolation=cv.INTER_CUBIC)

 frame = cv.GaussianBlur(frame, (15,15), cv.BORDER_DEFAULT) # 30


 # remember this to monitor the frame per second
 c_time = time.time() # updating the time
 fps = str(int(1/(c_time-p_time))) # calculating the fps
 p_time = c_time # saving the 


 cv.putText(frame, fps, (20,100), cv.FONT_HERSHEY_PLAIN, 5.0, (255,255,255), thickness=5)

 cv.imshow('video', frame)


 print(fps)

 # short cut
 if cv.waitKey(1) == ord('q'): # restricting it to being closed only when q is pressed
  break

 
# FONT_HERSHEY_PLAIN
# HERSHEY SIMPLEX
# HERSHEY PLAIN
# HERSHEY DUPLEX
# HERSHEY TRIPLEX
# HERSHEY COMPLEX SMALL
# HERSHEY SCIRPT SIMPLEX
# HERSHEY SCRIPT COMPLES