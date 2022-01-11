import cv2 as cv
import numpy as np


# img = cv.imread('cat.jpg')
img = np.zeros((500,500,3), dtype='uint8')

# --------------------------------------------------------- cv.FILLED -1
cv.rectangle(img, (100,100), (300,300), (0,255,0), thickness=1)

cv.circle(img,(300,300),200,(255,0,0),thickness=5)

cv.line(img, (200,200), (300,300),(0,0,255),thickness=4)

cv.putText(img,'(255,255)',(100,100),cv.FONT_HERSHEY_PLAIN,1.5,(255,255,0), thickness=1)


cv.imshow('drawing board', img)


cv.waitKey(0)

(470,650)
# write the shape of an image on the image on the top left corner
# check the video out also
# draw a rectangle
# draw a circle
# draw a line
# put some text 