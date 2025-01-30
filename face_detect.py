import cv2 as cv

img = cv.imread("Image//group.jpg")
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cas = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cas.detectMultiScale(grey,1.1,2)
print(f"number of faces found: {len(face_rect)}")

# draw rectangle over the faces
for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
cv.imshow("detech face",img)
cv.waitKey(0)

