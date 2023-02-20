import cv2
import face_recognition

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)
ret, img = cap.read()



c=1
while  ret==True:
    c=c+1
    ret,img=cap.read()
    #grpp = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + h, y + h), (0, 255, 0), 3)
    cv2.imshow('webcam',img)
    k=cv2.waitKey(1)
    print(img)
    if k==ord('q'):
        break;
print(c)

cap.release()
cv2.destroyAllWindows()