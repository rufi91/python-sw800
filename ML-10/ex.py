
#1. Write a program to apply translation with translation factors tx=200 and ty=100 on the image of apple
import cv2 as cv
import numpy as np

img =cv.imread('apple.jpg',0)
rows,cols= img.shape
M=np.float32([[1,0, 200],[0,1,100]])
dst= cv.warpAffine(img,M, (rows,cols))
#cv.imshow('dt',dst)
#cv.waitKey(0)

#2. Write a program apply scaling on the image of the apple with scaling factor 2 on both x and y axes.

img =cv.imread('apple.jpg')


dst= cv.resize(img,None,fx=2, fy=2, interpolation=cv.INTER_CUBIC)
#cv.imshow('dt',dst)
#cv.waitKey(0)

#3. Write a program to rotate the apple image 45 degrees

img =cv.imread('apple.jpg',0)
rows,cols= img.shape
M=cv.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), 45, 1)
dst= cv.warpAffine(img,M, (rows,cols))
#cv.imshow('dt',dst)
#cv.waitKey(0)

#4. Write a program to blend the images of apple and orange to get the image in result.jpg

aimg =cv.imread('apple.jpg')
oimg =cv.imread('orange.jpg')

aimg[:,256:,:]=oimg[:,256:,:]
#cv.imshow('dt',aimg)
#cv.waitKey(0)

#5. Write a program to obtain the negative of a grayscale image (hint:subtract 255 from all pixels values)
img =cv.imread('apple.jpg',0)

imght = img.shape[0]
imgwidth = img.shape[1]
img1=(img-128)
print img1

#cv.imshow('dt',img)
#cv.imshow('dt1',img1)
#cv.waitKey(0)


#6. Write a program to find out whether there is any difference between two images.

aimg =cv.imread('apple.jpg')
oimg =cv.imread('orange.jpg')
diff1=aimg-aimg
diff2= aimg-oimg
print diff1.sum()
print diff1.size, diff2.size


cv.imshow('dt',diff1)
cv.imshow('dt1',diff2)
cv.waitKey(0)

            
