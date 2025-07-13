import cv2
import os
import numpy
size=4
xml="facedet.xml"
images="datasets"
print("If you want your face to be recoginzed then you have to be in sufficient light")

(imglist,labellist,names,id)=([],[],{},0)
for(subdirs,dirs,files) in os.walk(images):
    for subdir in dirs:
        names[id]=subdir
        subpath=os.path.join(images,subdir)
        for filename in os.listdir(subpath):
            path=subpath+"/"+ filename
            label=id
            imglist.append(cv2.imread(path,0))
            labellist.append(int(label))
        id+=1
(width,height)=(100,130)
(imglist,labellist)=[numpy.array(lis) for lis in [imglist,labellist]]
model=cv2.face.LBPHFaceRecognizer_create()
model.train(imglist,labellist)
load=cv2.CascadeClassifier(xml)
webcam=cv2.VideoCapture(0)

while True:
    (_,im) = webcam.read()
    grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #detecting faces in the image
    faces=load.detectMultiScale(grey,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(56,78,56),2)
        face=grey[y:y+h,x:x+w]
        resizedimage=cv2.resize(face,(width,height))
        pred=model.predict(resizedimage)
        cv2.rectangle(im,(x,y),(x+w,y+h),(60,79,120),3)
        if pred[1]<500:
            cv2.putText(im,'% s- %.0f'%
                        (names[pred[0]],pred[1]),(x-10,y-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(255,255,255))
    cv2.imshow("title",im)
    key=cv2.waitKey(10)
    if key==27:
        break
webcam.release()
cv2.destroyAllWindows()

