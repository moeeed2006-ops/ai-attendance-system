import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# folder with known faces (one image per person)
path = 'known_faces'

images = []
classNames = []
fileNames = os.listdir(path)
print("Images found:", fileNames)

# read each image and pick the name from file
for f in fileNames:
    img = cv2.imread(f'{path}/{f}')
    if img is None:
        print("Could not read image:", f)
        continue
    images.append(img)
    classNames.append(os.path.splitext(f)[0])

print("Class Names:", classNames)


def findEncodings(imgList):
    # make encodings list for all known faces
    encodeList = []
    for oneImg in imgList:
        rgbImg = cv2.cvtColor(oneImg, cv2.COLOR_BGR2RGB)
        enc = face_recognition.face_encodings(rgbImg)
        if len(enc) > 0:          # simple check so it does not crash
            encodeList.append(enc[0])
        else:
            print("No face found in one of the images")
    return encodeList


def markAttendance(name):
    # save name with date and time in csv
    try:
        with open('Attendance.csv', 'r+') as f:
            data = f.readlines()
            nameList = []
            for line in data:
                entry = line.split(',')
                if len(entry) > 0:
                    nameList.append(entry[0])

            if name not in nameList:
                now = datetime.now()
                date = now.strftime('%Y-%m-%d')
                time = now.strftime('%H:%M:%S')
                f.write(f'\n{name},{date},{time}')
    except FileNotFoundError:
        # if file is not made yet just make it and write first line
        with open('Attendance.csv', 'w') as f:
            now = datetime.now()
            date = now.strftime('%Y-%m-%d')
            time = now.strftime('%H:%M:%S')
            f.write('Name,Date,Time')
            f.write(f'\n{name},{date},{time}')


print("Encoding faces, please wait...")
encodeListKnown = findEncodings(images)
print("Encoding Complete")

# open webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Could not read frame from camera")
        break

    # smaller image for speed
    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(img_small)
    encodesCurFrame = face_recognition.face_encodings(img_small, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc

            # scale back to original frame size
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            markAttendance(name)

    cv2.imshow('Webcam', img)

    # press Enter to quit
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
