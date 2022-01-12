import cv2 as cv
import numpy as np


# img = cv.imread('cat.jpg')
img = np.zeros((500,500,3), dtype='uint8')

# --------------------------------------------------------- cv.FILLED -1
#            frame  start     end        B, G, R    how thick -1 for filled
cv.rectangle(img, (100,100), (300,300), (0,255,0), thickness=1)

#         frame  center  radio  color  how thick?
cv.circle(img,(300,300),200,(255,0,0),thickness=5)

#      frame  start     end       color     how thick?
cv.line(img, (200,200), (300,300),(0,0,255),thickness=4)


#          frame YourTextHere  where to start from         scale  color
cv.putText(img,'(255,255)',(100,100),cv.FONT_HERSHEY_PLAIN,3.0,(255,255,0), thickness=5)
# how thick>
# bitwise operation

cv.imshow('drawing board', img)


cv.waitKey(0)

(470,650)
# write the shape of an image on the image on the top left corner
# check the video out also
# draw a rectangle
# draw a circle
# draw a line
# put some text 