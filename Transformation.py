import cv2 as cv
import numpy as np
img = cv.imread("Image//download.jpg")
cv.imshow("original",img)
# translation: shifting the img along the axis x and y meaning you can shift img up down left right, 
def translate(img,x,y):
    tranMat = np.float32([[1,0,x], [0,1,y]]) # 1 values ensure that the image is not scaled or rotated, 0 values ensure no shearing occurs.
    dimension = (img.shape[1], img.shape[0]) # size of the output image after the transformation.
    return cv.warpAffine(img, tranMat,dimension)


#  -x --> left
#  -y --> up
#  +x --> right
#  +y --> down

trans = translate(img,0,100)
cv.imshow("translated",trans)

# roation
def rotation(img, angle, rotation_point=None):
    (height,width) =img.shape[:2]

    # if the rotation point is none that mean we are going to rotate it around the center
    if rotation_point is None:
        rotation_point = (width//2, height//2)

        rotMat = cv.getRotationMatrix2D(rotation_point,angle,1.0)
        dimension = (width,height)

        return cv.warpAffine(img, rotMat,dimension)

rotate = rotation(img,45)
# cv.imshow("rotate",rotate)

# flip an img
flip = cv.flip(img,-1)
cv.imshow("flip",flip)
# flipcode = 0 mean vertical
# flipcode = 1 mean horizonal
# flipcode = -1 mean both vertical and horizonal




cv.waitKey(0)