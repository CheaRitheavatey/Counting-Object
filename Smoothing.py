import cv2 as cv

img = cv.imread("Image//download.jpg")
cv.imshow('img',img)
# what we need to know
# 1. kernal size = num of rows and nums of col in the pic

# method 1: averaging the middle kernal or the center will get the average intensity of those surrounding kernal 
average = cv.blur(img,(3,3))
cv.imshow("average",average)

# method 2: guassian blur: instead of calculating the average it, each surrounding pixel is given a weight and take the average weight => less blurring but more natural
guass = cv.GaussianBlur(img,(3,3),0)
cv.imshow("guass",guass)

# method 3: median blur: same as average but instead of average it find median instead. using not use for hight number like 5 or 7
median = cv.medianBlur(img,3)
cv.imshow("median",median)

# method 4: bilaterial: usually use in advance computer project, it apply blur but retain the edges
bilaterial = cv.bilateralFilter(img,3,15,15)
cv.imshow('bilaterial',bilaterial)
cv.waitKey(0)