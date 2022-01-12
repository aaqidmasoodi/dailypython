import cv2 as cv
import numpy as np

# Start here.
# 5 - 6 functions basics

img = cv.imread('cat.jpg')

# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # intensity distribution
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV) # thresholding...

# print(gray_img.shape)

# -------------------------------- KERNEL SIZE
blurred_img = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.blur()
# cv.medianBlur()

# egde detection -- CANNY EGDE DETECTOR >> 

# face video -------- blurred image
canny_img = cv.Canny(img, 0, 255) # check canny egde detector
# cv.Sobel()
# cv.Laplacian()

canny_img_blurred = cv.Canny(blurred_img, 0, 255)

cv.imshow('image', img)
cv.imshow('canny edges', canny_img)
cv.imshow('Blurred canny', canny_img_blurred)

# resize
# cv.resize()
# drawing a rectange 
# drawing a circle
# draw a line
# putting some onto an text


# cv.imshow('blurred Image', blurred_img)
# cv.imshow('gray image', gray_img)
# cv.imshow('hsv image', hsv_img)



cv.waitKey(0)