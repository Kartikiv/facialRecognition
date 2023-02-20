import cv2
import face_recognition
imgd=cv2.imread("iik.jpg")
rgb_img=cv2.cvtColor(imgd, cv2.COLOR_BGR2RGB)
img_encoding=face_recognition.face_encodings(rgb_img)[0]
img2= cv2.imread("C:\\Users\\karth\\OneDrive\\Desktop\\AADYA BIRTHDAY\\images.jpg")
rgb_img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2=face_recognition.face_encodings(rgb_img2)[0]
result=face_recognition.compare_faces([img_encoding],img_encoding2)
print(result)
