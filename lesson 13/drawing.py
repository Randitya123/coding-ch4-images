import cv2,numpy as np
#Range for the blue color
lowblue=np.array([100,150,0])
highblue=np.array([140,255,255])
canvas=None
prevpoint=None
capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()
    if not ret:
        break
    #fliping the frame
    frame=cv2.flip(frame,1)
    if canvas is None:
        canvas=np.zeros_like(frame)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lowblue,highblue)
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours and len(contours)>0:
        contour=max(contours,key=cv2.contourArea)
        if cv2.contourArea(contour)>100:
            M=cv2.moments(contour)
            if M["m00"]!=0:
                cx=int(M["m10"]/M["m00"])
                cy=int(M["m01"]/M["m00"])
                current=(cx,cy)
                if prevpoint is not None:
                    cv2.line(canvas,prevpoint,current,(255,0,0),5)
                prevpoint=current
        else:
            prevpoint=None
    else:
        prevpoint=None
    combined=cv2.add(frame,canvas)
    cv2.imshow("gfh",combined)
    cv2.imshow("title",mask)
    key=cv2.waitKey(1)
    if key==27:
        break
    elif key==ord('c'):
        canvas=None
        prevpoint=None
capture.release()
cv2.destroyAllWindows()
