#!/usr/bin/python

import sys
import cv2

import face_recognition

shan_image = face_recognition.load_image_file("shan.jpg")
shan_face_encoding = face_recognition.face_encodings(shan_image)[0]

ojas_image = face_recognition.load_image_file("ojas.jpg")
ojas_face_encoding = face_recognition.face_encodings(ojas_image)[0]

video_capture = cv2.VideoCapture(0)
counter = 0
face_names = []

while True:
    ret, image = video_capture.read()

    if not ret:
        break


    # Reduce face size to make calculations easier
    small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)

    # to save cpu, only do calculations once every 10 frames
    if counter % 3 == 0:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

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
        # Because we made the image smaller, now need to multiply by 4 to get correct size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(image, name, (left + 6, bottom - 6),  cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)
  

    cv2.imshow('Video', image)
    counter += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
