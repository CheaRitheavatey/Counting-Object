import cv2 as cv
import numpy as np

img= cv.imread("Image//download.jpg")

# convert to grey scale
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("grey",grey)

blur = cv.GaussianBlur(grey,(3,3),cv.BORDER_DEFAULT)

# edge detector using canny
canny = cv.Canny(blur,125,175)
cv.imshow("grey",canny)

# .findContours() = look at the structure of the canny and return 2 things contours and hierachy 
# contours, hierachies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.RETR_LIST = find all the contours in the img
# cv.RETR_EXTERNAL = find only the external contours
# cv.RETR_TREE = return all the hieracal contours

# cv.CHAIN_APPROX_NONE = how we want to approximate the contours, this return all the contours
# cv.CHAIN_APPROX_SIMPLE = compress all the contours to make sense
# print(len(contours))


# another method of contour

ret, thresh = cv.threshold(grey,125,255,cv.THRESH_BINARY)
# cv.imshow("thresh", thresh)
contours, hierachies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))


"""----------------------------------------------------"""
blank = np.zeros(img.shape, 'uint8')
cv.imshow("blank", blank)

cv.drawContours(blank,contours,-1,(255,255,255),1)
cv.imshow("",blank) # it similar to canny but not really
cv.waitKey(0) 