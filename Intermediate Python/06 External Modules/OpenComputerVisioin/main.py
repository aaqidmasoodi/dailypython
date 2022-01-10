import cv2 as cv
import numpy as np

# ---------------------------- RANGE?? 0-255
myimg = np.full((500,500), 255, dtype='uint8')

img = cv.imread('cat.jpg') # numpy array

# Resizing

# ---------------------------- W -- H
# .shape(row, column)
img_shape = img.shape

# Upscalling
resized_img = cv.resize(img, (img_shape[1]*2,img_shape[0]*2), interpolation=cv.INTER_CUBIC)

# Downscalling
resized_img = cv.resize(img, (img_shape[1]//4,img_shape[0]//4), interpolation=cv.INTER_CUBIC)

# Cropping 
# img = img[100:200, 200:300]

# imshow('window name', img(numpy array))
cv.imshow('myimage', myimg)

# to keep it open

print(type(img))
cv.waitKey(0)