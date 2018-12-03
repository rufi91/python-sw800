"""
Apply adaptive thresholding to make the sudoku.jpg image more reader. Try
to do the same with other similar images.
"""

import cv2 as cv

img=cv.imread('sudoku.jpg',0)
print img.shape
img1=cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
cv.imshow("dt",img1)
cv.waitKey(0)
