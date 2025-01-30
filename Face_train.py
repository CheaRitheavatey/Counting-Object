import os
import cv2 as cv
import numpy as np

people = ['Bakugo','Midoriya', 'Todoroki'] 
DIR = r'C:\\Users\\Admin\\Documents\\GitHub\\Counting-Object\\Faces'
feature = []
labels = []

haar_cas = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)

            if img_array is not None:
                grey = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            else: 
                print("error")

            face_rect = haar_cas.detectMultiScale(grey,1.1,4)

            for (x,y,w,h) in face_rect:
                faces_roi = grey[y:y+h, x:x+w]

                
                feature.append(faces_roi)
                labels.append(label)


create_train()
feature = np.array(feature,dtype='object')
labels = np.array(labels)
face_recongizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the feature list and the labels list
face_recongizer.train(feature, labels)

face_recongizer.save('face_trained.yml')
np.save('feature.npy',feature)
np.save('labels.npy',labels)
