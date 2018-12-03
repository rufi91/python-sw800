"""
Blend the images OpenCVLogo.png and ml.png using addWeighted function
in a 0.7:0.3 ratio. Try the same with other images
"""
import cv2 as cv

img1=cv.imread('ml.png')
img2=cv.imread('opencv-logo.png')

dt=cv.addWeighted(img1,.7, img2, .3,0)
cv.imshow("dt",dt)
cv.waitKey(0)
