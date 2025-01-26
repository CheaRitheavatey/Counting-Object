import cv2 as cv
import numpy as np

"""-------------------draw on image------------------------"""
# if we want a blank image
blank = np.zeros((500,500,3), dtype='uint8') # uint8 = image
# cv.imshow("blank",blank)

# img = cv.imread("Image//download.jpg")
# cv.imshow("picture",img)

# set color to the blank canva
blank[:] = 0,255,0 # rgb number
# cv.imshow("green",blank)

# draw rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,123),cv.FILLED)
# or we can do blank.shape[0] // 2 instead of (250,250) or something like that
# cv.imshow("rectangle",blank)


# draw circle
cv.circle(blank,(blank.shape[1] // 2, blank.shape[0] //2), 40, (255,0,0),cv.FILLED)
# cv.imshow("circle",blank)

# draw line
cv.line(blank,(0,0),(250,250),(0,0,0),3)
# cv.imshow("line",blank)

# draw a text
cv.putText(blank,"Hello",(225,225),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255),3)
cv.imshow("text", blank)
cv.waitKey(0)