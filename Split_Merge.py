import cv2 as cv
import numpy as np

img = cv.imread("Image//download.jpg")

# split the color into blue green red
b,g,r = cv.split(img)


# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)
# it will show it in grey scale and when it is lighter that mean that color is dominant in that part and when its darker that mean it doesnt have that color in that region

# merge
merge = cv.merge([b,g,r])
# cv.imshow('merge',merge) # when we merge back it will go  back to original color

# there is a way to show red green and blue and not the greyscale

# 1 create a blank canvas
blank = np.zeros(img.shape[:2],dtype='uint8')
# merge each color to the blank canvas
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)


cv.waitKey(0)