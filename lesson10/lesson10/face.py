import cv2,os
xml="facedet.xml"
data="datasets"
subdata="Randitya"
path=os.path.join(data,subdata)
#if the folder does not exist, creating one
if not os.path.isdir(path):
    os.mkdir(path)
#standard size for image
(width,height)=(100,150)
#loading cascade face detection
cascade=cv2.CascadeClassifier(xml)
webcam=cv2.VideoCapture(0)
count=1
while count < 30:
    (_,im) = webcam.read()
    grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #detecting faces in the image
    faces=cascade.detectMultiScale(grey,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(56,78,56),2)
        face=grey[y:y+h,x:x+w]
        resizedimage=cv2.resize(face,(width,height))
        cv2.imwrite('%s/%s.png' % (path, count), resizedimage)
    count+=1
    cv2.imshow("title",im)
    key=cv2.waitKey(10)
    if key==27:
        break