# import cv2
import cv2 as cv
"""----------------------read image----------------------------------"""
# .imread()
img = cv.imread('Image//download.jpg')

# .imshow()
cv.imshow("Dog",img)

# .waitkey(0)
cv.waitKey(0)

"""----------------------read video---------------------------------"""
# know where the path is
capture = cv.VideoCapture("Image//IMG_0014.MP4")

while True:
    isTrue, frame = capture.read() # read the video frame by frame, isTrue is a boolean to determine if the frame is successfully read or not 
    cv.imshow("Video",frame) # display each frame of the video using .imshow()

    # to break out this while loop we use if
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
capture.release() # release capture pointer
cv.destroyAllWindows() 