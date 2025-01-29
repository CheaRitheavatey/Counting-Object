import cv2 as cv
# take img and convert to binary img = threshold

img = cv.imread("Image//download.jpg")

# 1. simple threshold
# first we have to convert the img to greyscale
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
threshold, thresh = cv.threshold(grey,150,255,cv.THRESH_BINARY)
# cv.imshow("simple threshold",thresh)

threshold, thresh_inverse = cv.threshold(grey,150,255,cv.THRESH_BINARY_INV)
# cv.imshow("simple threshold inverse",thresh_inverse) # inverse black and white part

# 2. adpative thresholding: the computer find the optimal threshold value and we dont have to put the number manually
# first we still have to convert the img to greyscale
adaptive_thresh = cv.adaptiveThreshold(grey,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive thresh',adaptive_thresh)


cv.waitKey(0)
