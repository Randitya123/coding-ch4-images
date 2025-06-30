import cv2 as cv2, numpy as np, time

print(cv2.__version__)
#opening the viodeo file 
open=cv2.VideoCapture(r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4\lesson8\video.mp4")
time.sleep(2)
counter=0
bg=0
#capturing bg without the person
for dt in range(60):
    value,bg=open.read()
    if value==False:
        continue
    bg=cv2.rotate(bg,cv2.ROTATE_90_COUNTERCLOCKWISE)

#framebyframeread
while(open.isOpened()):
    value,img=open.read()
    if value==False:
        break
    counter+=1
    img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
    #changing the colors
    color=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #detecting range of red
    lowred=np.array([100,40,40])
    highred=np.array([100,255,255])
    #creating a mask for the red color
    mask1=cv2.inRange(color,lowred,highred)
    lowred=np.array([155,40,40])
    highred=np.array([180,255,255])
    #creating a mask for the red color
    mask2=cv2.inRange(color,lowred,highred)
    mask1=mask1+mask2
    #cleaning up the mask
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN, np.ones((3,3),np.uint8), iterations=2)
    mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
    #creating the oppsoite mask
    mask2=cv2.bitwise_not(mask1)
    onlred=cv2.bitwise_and(bg,bg ,mask=mask1)
    result=cv2.bitwise_and(img,img,mask=mask2)
    #final output
    finaloutput=cv2.addWeighted(onlred,1,result,1,0)
    cv2.imshow("TITLE",finaloutput)
    k =cv2.waitKey(10)
    if k==27:
        break
    
    
