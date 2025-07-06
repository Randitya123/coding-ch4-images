import cv2
rt=cv2.VideoCapture("cars.mp4")
xml=cv2.CascadeClassifier("car.xml")
#themainloop
while True:
    ret, frames=rt.read()
    if not ret:
        break
    greyimg=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cars=xml.detectMultiScale(greyimg,scaleFactor=1.1,minNeighbors=1)
    #looping the throug all detected images
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(40,80,135),2)
    cv2.imshow("title",frames)
    if cv2.waitKey(33)==27:
        break
#realsing memory
rt.release()
cv2.destroyAllWindows()