import cv2, numpy as np,os,random,time

capture=cv2.VideoCapture(0)
ret,frame1=capture.read()
ret,frame2=capture.read()

list1=[]
totalballons=10
score=0

for i in range(totalballons):
    xballon=random.randint(100,500)
    yballon=random.randint(100,500)
    radius=random.randint(30,50)
    list1.append({'x':xballon,'y':yballon,"r":radius,'popped':False})
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
while True:
    difference=cv2.absdiff(frame1,frame2)
    greyimg=cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
    blurredimg=cv2.GaussianBlur(greyimg,(5,5),0)
    _,thresh=cv2.threshold(blurredimg,20,255,cv2.THRESH_BINARY )
    diltedimg=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(diltedimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    frame=frame1.copy()
    #drawing the unpoped ballons
    for i in list1:
        if not i['popped']:
            cv2.circle(frame,(i['x'],i['y']),i['r'],(49,90,84),-1)
    for k in contours:
        if cv2.contourArea(k)<1500:
            continue
        x,y,w,h=cv2.boundingRect(k)
        center=(x+w // 2,y+h // 2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        for i in list1:
            if not i['popped']:
                distance=np.linalg.norm(np.array(center)-np.array((i['x'],i['y'])))
                if distance<i["r"]+10:
                    i["popped"]=True
                    score+=1
    cv2.putText(frame,f"Score:{score}",(10,30),font,1,(20,123,178))
    cv2.imshow("title",frame)
    frame1=frame2
    ret,frame2=capture.read()
    key=cv2.waitKey(30)
    if key==27:
        break
    elif key==ord('r'):
        list1=[]
        score=0
        for i in range(totalballons):
            xballon=random.randint(100,500)
            yballon=random.randint(100,500)
            radius=random.randint(30,50)
            list1.append({'x':xballon,'y':yballon,"r":radius,'popped':False})
capture.release()
cv2.destroyAllWindows()
