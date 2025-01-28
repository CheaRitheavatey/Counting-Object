import cv2 as cv
import numpy as np

img = cv.imread("Image//download.jpg")
# using bit wise operation we can do masking which allow us to focus on specific place in the img. example we want to focus on people face in the img and remove all the other part

blank = np.zeros(img.shape[:2],'uint8')

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("mask",mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked image",masked)

cv.waitKey(0)