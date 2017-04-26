#!/usr/bin/python

import sys
import cv2


imgpath = sys.argv[1]
cascasdepath = "haarcascade_frontalface_default.xml"

image = cv2.imread(imgpath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cascasdepath)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (30,30)

    )

print("The number of faces found = ", len(faces))

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+h, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)    
cv2.waitKey(0)