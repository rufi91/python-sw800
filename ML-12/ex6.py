

import cv2 as cv
import numpy as np

ban_cascade=cv.CascadeClassifier('banana.xml')


img=cv.imread('i2.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print ban_cascade


bans = ban_cascade.detectMultiScale(gray, 12,5)
print bans

for (x,y,w,h) in bans:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


cv.imshow('dt',img)
cv.waitKey(0)
