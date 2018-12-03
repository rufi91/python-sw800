"""
Make the opencvlogo smoother by applying blur function. Try it with other
images.
"""

import cv2 as cv

img1=cv.imread('/home/ai21/Ex-Rufza/ML/ML-12/opencv-logo.png')
blur=cv.blur(img1,(20,20))
cv.imshow("dt", blur)
cv.waitKey(0)
