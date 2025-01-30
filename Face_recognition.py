import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Bakugo','Midoriya', 'Todoroki']
# feature = np.load('feature.npy',allow_pickle=True)
# labels = np.load('labels.npy',allow_pickle=True)

face_recongizer = cv.face.LBPHFaceRecognizer_create()
face_recongizer.read('face_trained.yml')

img = cv.imread('C:\\Users\\Admin\\Documents\\GitHub\\Counting-Object\\Faces\\Bakugo\\images.jpg')

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("person",grey)

# detect the face
face_rect = haar_cascade.detectMultiScale(grey,1.1,4)

for (x,y,w,h) in face_rect:
    faces_roi = grey[y:y+h, x:x+w]
    label,confidence = face_recongizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow("face detection",img)
cv.waitKey(0)