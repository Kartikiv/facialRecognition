import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img= cv2.imread("C:\\Users\\karth\\OneDrive\\Desktop\\AADYA BIRTHDAY\\images.jpg")

#cv2.imshow("BN2B3665",img)
res=cv2.resize(img,(int(img.shape[1]*1),int(img.shape[0]*1)))
gary=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#print(img.shape)
faces=face_cascade.detectMultiScale(gary,scaleFactor=1.15,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
 res= cv2.rectangle(res, (x,y), (x+h,y+h), (0,255,0), 3)
#es=cv2.resize(img,int(img.shape[1]/4),int(img.shape[0]/4))
cv2.imshow("lop",res)
cv2.waitKey(0)
cv2.destroyAllWindows()