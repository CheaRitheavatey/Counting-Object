import cv2 as cv



# we can create a method to rescale frame
def rescaleFrame(frame, scale=0.75): # scale 0.75 = reduce size to 75% of the original
    width = int(frame.shape[1] * scale) # we can int() the width and height
    height = int(frame.shape[0] * scale)

    dimension = (width,height) # the new dimension of the frame

    # reside the frame to a particular dimension
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

"""-------------------resize image------------------------"""
# img = cv.imread("Image//download.jpg")
# resize = rescaleFrame(img)
# cv.imshow("picture", img)
# cv.imshow("resize",resize)

# cv.waitKey(0)

"""-------------------resize video------------------------"""
cap = cv.VideoCapture("Image//IMG_0014.MP4")
while True:
    istrue, frame = cap.read()
    resizeframe = rescaleFrame(frame) # resize the video frame
    cv.imshow("video",frame)
    cv.imshow("resize video", resizeframe) # show the resize the video frame

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

"""-------------------resize for live video------------------------"""
def changeRes(width,height):
    cap.set(3,width) # using .set() meaning set width to 3 and set height to 4
    cap.set(4,height) # using .set() can only work with live video only
