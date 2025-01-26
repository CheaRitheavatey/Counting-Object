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
    - width is frame.shape[1]
    - height is frame.shape[0]
    - we can also convert the width and height into int
    - 1: import cv2
    - 2: width = int(frame.shape[1] * scale) # we can int() the width and height
    - 3: height = int(frame.shape[0] * scale)
    - 4: dim = (width, height)
    - 5: resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

- how to resize and rescale a video
    - 1: import cv2
    - 2: width = int(frame.shape[1] * scale) # we can int() the width and height
    - 3: height = int(frame.shape[0] * scale)
    - 4: dim = (width, height)
    - 5: resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA) 
    - 6: while cap.isOpened(): 
    - 7: ret, frame = cap.read()
    - 8: if ret == True:
    - 9: resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    - 10: cv2.imshow('frame',resized)
    - 11: if cv2.waitKey(1) & 0xFF == ord('q'):
    - 12: break

- how to draw on image
    - 1: import cv2
    - 2: img = cv2.imread('image.jpg')
    - 3: cv2.line(img,(0,0),(150,150),(0,255,0),3)
    - 4: cv2.rectangle(img,(15,25),(200,150),(0,0,255),cv2.FILLED)
    - 5: cv2.circle(img,(400,50),30,(255,255,0),5)
    - 6: cv2.putText(img,'OpenCV',(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)