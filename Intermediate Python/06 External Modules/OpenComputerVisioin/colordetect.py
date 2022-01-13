import cv2 as cv
import numpy as np

img = cv.imread('cosco.jpg')
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), cv.INTER_CUBIC)


img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


low_green = np.array([36, 63, 25]) # -->> olive green to white
high_green = np.array([70, 255,255])

green_mask = cv.inRange(img_hsv, low_green, high_green)


masked_img = cv.bitwise_and(img, img, mask=green_mask) # noise 

cv.imshow('img', img)
cv.imshow('green_mask', green_mask)
cv.imshow('ball', img_hsv) # this expect always an rgb
cv.imshow('green_filter', masked_img)


cv.waitKey(0)


# DETECT BLUE FROM LIVE WEBCAM FEED ISOLATION ONLY BLUE PEN CAP