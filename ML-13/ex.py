"""
1) Try to remove the noise from the man.jpg image by doing erosion
and dilation in a sequence.
2) Try to remove the noise from the man.jpg by using
morphologyEx() function. Get resultantant images for the two
arguments
a. cv.MORPH_close
b. cv.MORPH_open
"""
#1

import cv2 as cv
import numpy as np


img=cv.imread('man.jpg',0)
kernel=np.ones((3,3), np.uint8)
erode= cv.erode(img, kernel, iterations=5)
dialate=cv.dilate(img,kernel,iterations=2)
img1=np.hstack((img,erode, dialate))
#cv.imshow('dt', img1)
#cv.waitKey(0)

#2
morph= cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
morph1= cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
img2=np.hstack((img,morph,morph1))
#cv.imshow('dt', img2)
#cv.waitKey(0)

"""
3) Do noise removal in the girl.jpg image using the above program.
4) Apply sobel feature detection functions on the ‘building.png’
picture
"""
#3
imggirl=cv.imread('girl.jpg',0)
morphg= cv.morphologyEx(imggirl, cv.MORPH_OPEN, kernel)
morphg1= cv.morphologyEx(imggirl, cv.MORPH_CLOSE, kernel)
img3=np.hstack((imggirl,morphg,morphg1))
#cv.imshow('dt', img3)
#cv.waitKey(0)

#4
imgBuild=cv.imread('building.png')
print imgBuild.shape
sobelx=cv.Sobel(imgBuild, cv.CV_32F,1,0,ksize=1)
sobely=cv.Sobel(imgBuild, cv.CV_32F,0,1,ksize=1)
imgBuild=np.hstack((imgBuild,sobelx,sobely))
cv.imshow('dt',imgBuild)
cv.waitKey(0)
