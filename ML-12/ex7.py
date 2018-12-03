"""
Apply edge detection algorithm canny on the messi.jpg image.
"""

import cv2 as cv

img=cv.imread('i2.jpg')
edge= cv.Canny(img, 200,200)

cv.imshow('dt',edge)
cv.waitKey(0)
