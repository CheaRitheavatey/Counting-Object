import cv2 as cv
img = cv.imread("Image//download.jpg")


# converting image to grey scale
# grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# blur the image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) # ksize has to be odd number the higher the number the blurier it get

# edge cascade
canny = cv.Canny(blur,125,175)
# cv.imshow("canny", canny)
# to get rid some of the edges using canny we can pass blur instead of img 

# dialting the image
dilated = cv.dilate(canny,(3,3), iterations=1)
# cv.imshow("dialate",dilated)

# erdoing
erode = cv.erode(dilated,(3,3),iterations=1)
# cv.imshow("erode",erode)

# resize
resize= cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR) #linear is for small img to bigger img,cv.INTER_AREA is for bigger img to smaller img 
# cv.imshow("resize",resize)

# cropping img: by array slicing meaning you slice the image from what index to what index
crop = img[0:100, 100:200]
cv.imshow("crop",crop)

cv.waitKey(0)