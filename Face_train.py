import os
import cv2 as cv
import numpy as np

people = ['Midoriya', 'Bakugo', 'Todoroki']
DIR = r'C:\\Users\\Admin\\Documents\\GitHub\\Counting-Object'
feature = []
labels = []

haar_cas = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR,people)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            grey = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            face_rect = haar_cas.detectMultiScale(grey,1.1,4)

            for (x,y,w,h) in face_rect:
                faces_roi = grey[y:y+h, x:x+w]
                feature.append(faces_roi)
                labels.append(label)


create_train()
print(f"length of the feature = {len(feature)}")
print(f"length of the labels = {len(labels)}")