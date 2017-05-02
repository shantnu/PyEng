#!/usr/bin/python

import sys
import cv2


shan_image = face_recognition.load_image_file("shan.jpg")
shan_face_encoding = face_recognition.face_encodings(shan_image)[0]

ojas_image = face_recognition.load_image_file("ojas.jpg")
ojas_face_encoding = face_recognition.face_encodings(ojas_image)[0]

video_capture = cv2.VideoCapture(0)


while True:
    ret, image = video_capture.read()

    if not ret:
        break

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce face size to make calculations easier
    #smaller_frame = cv2.resize(frame, (0, 0), fx=0.1, fy=0.1)

    face_locations = face_recognition.face_locations(gray)
    face_encodings = face_recognition.face_encodings(gray, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([shan_face_encoding, ojas_face_encoding], face_encoding)
        name = "Unknown"

        if match[0]:
            name = "shantnu"
        elif match[1]:
            name = "ojas"

        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
  

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()