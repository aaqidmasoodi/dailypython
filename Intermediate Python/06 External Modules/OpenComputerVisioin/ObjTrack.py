import cv2 as cv
import numpy as np

capture = cv.VideoCapture('car.mp4')

while True:
 ret, frame = capture.read()

 # loops the video
 if not ret:
  capture = cv.VideoCapture('car.mp4')
  ret, frame = capture.read()

 # converting to HSV
 hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


 low_b = np.array([127, 69, 63])
 high_b = np.array([290,359,359])

 # color mask
 color_mask = cv.inRange(hsv_frame, low_b, high_b)


 # detect contours
 contours, _ = cv.findContours(color_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 

 for contour in contours:
  if cv.contourArea(contour) > 1000:
   x, y, x1, y1 = cv.boundingRect(contour) # media
   cv.rectangle(frame, (x-50,y-50), (x+x1+50,y+y1+50), (0,255,0), 2)


 cv.imshow('Video', frame)
 cv.imshow('mask', color_mask)


 if cv.waitKey(30) == ord('q'):
  break



# HEADING TOWARDS
# 10X
# ML & AI # Robotics
# DNN
# AlphaZero - GO/Chess/Shogi


# Machine Learning


# WORKING WITH NUMPY 
# WORKING WITH OPENCV



