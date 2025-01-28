import cv2 as cv
# import matplotlib.pyplot as plt

img = cv.imread("Image//download.jpg")
cv.imshow("img",img)

# plt.imshow(rgb)
# plt.show()

# BGR to greyscale
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("grey",grey)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# we can also inverse the coversion as well.
# example we can convert grey to BGR, HSV to BGR, RGB to BGR...




cv.waitKey(0)