import cv2 as cv
import numpy as np

img = cv.imread("Image//download.jpg")
# method 1: laplacian

# step 1 : convert to grey scale
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# step 2: .laplacian
lap = cv.Laplacian(grey,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)

# method 2: subel: compute gradient into 2 direction
# step 1: covert to greyscale

sobelx = cv.Sobel(grey,cv.CV_64F,1,0)
sobely = cv.Sobel(grey,cv.CV_64F,0,1)

combine_sobel = cv.bitwise_or(sobelx,sobely)

# cv.imshow('sobel x', sobelx)
# cv.imshow('sobel y', sobely)
cv.imshow("combine sobel", combine_sobel)

# lets compare with canny edge detector
canny = cv.Canny(grey,150,175)
cv.imshow("Canny",canny)

cv.waitKey(0)
