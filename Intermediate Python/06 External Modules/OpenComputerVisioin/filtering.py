# Try this as an Assignment where you try to contour detect the red ball
import cv2 as cv
import tkinter as tk # tkinter is bultin to python # swing
import numpy as np

window = tk.Tk()

label_low = tk.Label(window, text='LOWER BOUND',pady=30)

# creating three sliders for HUE, SATURATION, VALUE for LowerB
low_H = tk.Scale(window, from_=0, to=359, orient='horizontal')
low_S = tk.Scale(window, from_=0, to=359, orient='horizontal')
low_V = tk.Scale(window, from_=0, to=359, orient='horizontal')

label_low.pack()
low_H.pack()
low_S.pack()
low_V.pack()


# i've also added some labels and stuff for your understanding...
# low_h.set(int) # to set an initial value for a slider

label_high = tk.Label(window, text='HIGHER BOUND', pady=30)

# creating three sliders for HUE, SATURATION, VALUE for UpperB
High_H = tk.Scale(window, from_=0, to=359, orient='horizontal')
High_S = tk.Scale(window, from_=0, to=359, orient='horizontal')
High_V = tk.Scale(window, from_=0, to=359, orient='horizontal')

label_high.pack()
High_H.pack()
High_S.pack()
High_V.pack()



capture = cv.VideoCapture('rev balls.mp4')


while True:
 ret, frame = capture.read()

 # resetting the video
 if not ret:
  capture = cv.VideoCapture('rev balls.mp4')
  ret, frame = capture.read()

 hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

 # lowerB
 low_b = np.array([low_H.get(), low_S.get(), low_V.get()])

 # HigherB
 high_b = np.array([High_H.get(), High_S.get(), High_V.get()])

 # creating the mask
 mask = cv.inRange(hsv_frame, low_b, high_b)


 # filtering out

 filtered_frame = cv.bitwise_and(frame, frame, mask=mask)




 cv.imshow('Video', frame)
 cv.imshow('filter', filtered_frame)


 window.update()# tkinter window is being updated
 if cv.waitKey(30) == ord('q'):
  break 


capture.release()
cv.destroyAllWindows()