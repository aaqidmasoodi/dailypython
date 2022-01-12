import cv2 as cv
import numpy as np

canvas_img = np.zeros((500,500), dtype='uint8')

square_img = canvas_img.copy()
circle_img = canvas_img.copy()

cv.rectangle(square_img, (20,20), (480,480), 255, thickness=cv.FILLED)
cv.circle(circle_img, (250,250), 250, 255, thickness=cv.FILLED)


intersection_img = cv.bitwise_xor(square_img, circle_img)

# DIY
# cv.bitwise_or()
# cv.bitwise_not()
# cv.bitwise_xor() # ??


# 0 0 0
# 1 1 0

cv.imshow('Square', square_img)
cv.imshow('Circle', circle_img)
cv.imshow('Intersection (AND)', intersection_img)


cv.waitKey(0)