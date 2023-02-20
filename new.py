import cv2
import face_recognition
vid = cv2.VideoCapture(0)
ll, ikl = vid.read()

while ll==True:
    ll, ikl = vid.read()
    print(ll)
    print(ikl)
    cv2.imshow('ikl', ikl)
    key=cv2.waitKey(10)
    if key==ord('k'):
        break
cv2.destroyAllWindows()