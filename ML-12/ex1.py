"""
1) Write a program to apply various thresholding operations on the image
gradient.jpg. Apply the same with other similar images and analyze the
results.
THRESH_BINARY
THRESH_BINARY_INV
THESH_TRUNC
THRESH_TOZERO
THRESH_TOZERO_INV
"""

import cv2 as cv
img= cv.imread('gradient.jpg')
ret, th1= cv.threshold(img, 127,255, cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

cv.imshow('dt', thresh3)
cv.waitKey(0)

