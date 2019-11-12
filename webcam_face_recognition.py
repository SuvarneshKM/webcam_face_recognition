import cv2
import time

video = cv2.VideoCapture(0)


check,frame = video.read()


gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier("C:\\Users\\suvar\\Desktop\\img\\haarcascade_frontalface_default.xml")

faces = cascade.detectMultiScale(gray_frame,scaleFactor = 1.05,minNeighbors=5)

time.sleep(3)
    
    

for x,y,w,h in faces:
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('capture', frame)

cv2.waitKey(0)
        


video.release()

cv2.destroyAllWindows()
