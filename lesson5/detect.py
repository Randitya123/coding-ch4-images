import cv2
import numpy as np

dt=cv2.imread("eye.webp",1)
at=cv2.cvtColor(dt,cv2.COLOR_BGR2GRAY)
#making the image a little blurry
blurese=cv2.blur(at,(3,3))
#detetcting circle
circ=cv2.HoughCircles(blurese,cv2.HOUGH_GRADIENT,1,12,param1=50,param2=30,minRadius=10,maxRadius=30)
if circ is not None:
    circ=np.uint16(np.around(circ))
    for i in circ[0,:]:
        pos1,pos2,radiuss=i[0],i[1],i[2]
        cv2.circle(dt,(pos1,pos2),radiuss,(67,89,234),3)
        cv2.circle(dt,(pos1,pos2),1,(67,89,234),3)
        cv2.imshow("TITLE",dt)
        cv2.waitKey(0)
        
