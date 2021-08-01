# Objective: Apply the haar cascade trained model on a validation image
import numpy as np
import cv2 as cv
import os

people = []
DIR = r'Data\faces\train'
for i in os.listdir(DIR):
    people.append(i)


haar_cascade = cv.CascadeClassifier('haar_face.xml')

#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# read the pre-trained model
face_recognizer.read('face_trained.yml')
img = cv.imread(r'Data\Faces\val\elton_john\1.jpg')
#img = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]}  with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),
               thickness =2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)