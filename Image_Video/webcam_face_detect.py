#!/usr/bin/python

import sys
import cv2


cascasdepath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascasdepath)

if len(sys.argv) < 2:
    video_capture = cv2.VideoCapture(0)
else:
    video_capture = cv2.VideoCapture(sys.argv[1])

while True:
    ret, image = video_capture.read()

    if not ret:
        break

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
