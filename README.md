# OpenCV
- OpenCV is a library of programming functions mainly aimed at real-time computer vision applications.

- how to read an image in opencv:
    - 1: import cv2
    - 2: img = cv2.imread('image.jpg')
    - 3: cv2.imshow('image',img)
    - 4: cv2.waitKey(0)

- how to read video in opencv:
    - 1: import cv2
    - 2: cap = cv2.VideoCapture('video.mp4') # (0) for webcam
    - 3: while cap.isOpened(): 
    - 4: ret, frame = cap.read()
    - 5: if ret == True:
    - 6: cv2.imshow('frame',frame)
    - 7: if cv2.waitKey(1) & 0xFF == ord('q'):
    - 8: break

- how to resize and rescale an image