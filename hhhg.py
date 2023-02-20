import cv2
import numpy as np
import face_recognition
import os
path='E:\karth\PycharmProjects\pythonProject1\pop'
images= []
classnames= []
myList=os.listdir(path)
print(myList)
for cls in myList:
    crrimg=cv2.imread(f'{path}/{cls}')
    images.append(crrimg)
    classnames.append(os.path.splitext(cls)[0])
print(classnames)

def findenc(images):
    encodeList=[]
    for img in images:
         img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
         encode = face_recognition.face_encodings(img)[0]
         encodeList.append(encode)
    return encodeList
encodeListknown= findenc(images)
print(len(encodeListknown))
cap1=cv2.VideoCapture(0)

while True:
    sucess, img=cap1.read()
    imgS=cv2.resize(img,(0,0),None,0.33,0.33)
    imgS= cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facescurframe= face_recognition.face_locations(imgS)
    encode1 = face_recognition.face_encodings(imgS,facescurframe)
    for encodeFace,faceloc in zip(encode1,facescurframe):
        match = face_recognition.compare_faces(encodeListknown,encodeFace)
        facedist=face_recognition.face_distance(encodeListknown,encodeFace)
   #     print(facedist)
        matchIndex=np.argmin(facedist)
        if match[matchIndex]:
            name = classnames[matchIndex]
          #  print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2, y2, x1=y1*3,x2*3,y2*3,x1*3

            cv2.rectangle(img, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
           # cv2.imshow('web', img)




    cv2.imshow('shw', img)
    cv2.waitKey(80)
