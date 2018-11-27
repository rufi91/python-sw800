"""
1) Create a black image of 512X512 dimension and fill region 50X50 with
green color.
2) Create a black image of 512X512 dimension.
a. Add a line from the point (10,1) to (500,100)
b. Draw a rectangle with corner points at (10,1) and (500,100)
"""

import cv2 as cv
import numpy as np


img=np.zeros((512,512, 3), np.uint8)
img[:50,:50]=(0,255,0)
cv.line(img, (10,1), (500,100), (255,255,150), 5)
cv.rectangle(img, (10,1),(500,100), (150,150,150), 2)

cv.imshow('d1',img)
k=cv.waitKey(0)
