# contours & masks
import cv2 as cv
import numpy as np

ball_img = cv.imread('cosco.jpg')
ball_img = cv.resize(ball_img, (ball_img.shape[1]//2, ball_img.shape[0]//2), interpolation=cv.INTER_CUBIC)

# how to use a mask with bitwise operation

# rewrite this in a simpler way

our_mask = np.zeros(ball_img.shape, dtype='uint8')
# cv.rectangle(our_mask, (300, 150), (150, 600), 255, -1)
cv.circle(our_mask, (250,250), 200, (255,255,255), -1)




masked_img = cv.bitwise_and(ball_img, our_mask)


cv.imshow('ball', ball_img)
cv.imshow('mask', our_mask)
cv.imshow('masked_img', masked_img)


cv.waitKey(0)