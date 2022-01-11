import cv2 as cv
import numpy as np

blank_img = np.zeros((500,500,3), dtype='uint8')
blank_img[100:250, 150:300] = 50,20,40

cv.imshow('myimage', blank_img)


cv.waitKey(0)