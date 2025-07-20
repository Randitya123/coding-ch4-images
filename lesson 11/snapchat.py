import cv2,numpy as np, os
cascade=cv2.CascadeClassifier(r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4\lesson 11\facedet.xml")
#print(os.path,exists(cv2.data.haarcascades+"facedet.xml"))
glassesimg=cv2.imread("glass.png",cv2.IMREAD_UNCHANGED)
height,width=glassesimg.shape[:2]
aspectratio=width/height
def sepia(frame):
    filter1=np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    frames=cv2.transform(frame,filter1)
    return np.clip(frames,0,255).astype(np.uint8)

def cartoon(frame):
    greyimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurredimg=cv2.medianBlur(greyimg,3)
    edges=cv2.adaptiveThreshold(blurredimg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color=cv2.bilateralFilter(frame,7,300,300)
    cartoon=cv2.bitwise_and(color,color,mask=edges)
    return cartoon

def glasses(bg,overlay,x,y):
    bh,bw=bg.shape[:2]
    h,w=overlay.shape[:2]
    if x+w>bw or y+h> bh or x<0 or y<0:
        return bg
    transperacny=overlay[:,:,3]/255.0
    for i in range(3):
        bg[y:y+h,x:x+w,i]=((1 - transperacny) * bg[y:y+h, x:x+w, i] + transperacny * overlay[:, :, i])
    return bg

capture=cv2.VideoCapture(0)
filtertype="ORIGINAL"
print("Press keys to apply filters:")
print("0-ORIGINAL")
print("1-GREY SCALE")
print("2-SEPIA")
print("3-NEGATIVE")
print("4-CARTOON")
print("5-GLASSES")
print("Q-QUIT")

while True:
    ret,frame=capture.read()
    if not ret:
        break
    #appling selected filter
    if filtertype=="GREY SCALE":
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    elif filtertype=="SEPIA":
        frame=sepia(frame)
    elif filtertype=="NEGATIVE":
        frame=cv2.bitwise_not(frame)
    elif filtertype=="CARTOON":
        frame=cartoon(frame)
    elif filtertype=="GLASSES":
        greyscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(greyscale,1.1,5)
        for(x,y,w,h) in faces:
            dw=w
            dh=int(dw/aspectratio)
            rg=cv2.resize(glassesimg,(dw,dh))
            gy=y
            frame=glasses(frame,rg,x,gy)
    if isinstance(frame,np.ndarray) and len(frame.shape)==2:
        frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    cv2.imshow("title",frame)
    key=cv2.waitKey(1)& 0xFF
    if key==ord('0'):
        filtertype="ORIGINAL"
    elif key==ord('1'):
        filtertype="GREY SCALE"
    elif key==ord('2'):
        filtertype="SEPIA"
    elif key==ord('3'):
        filtertype="NEGATIVE"
    elif key==ord('4'):
        filtertype="CARTOON"
    elif key==ord('5'):
        filtertype="GLASSES"
    elif key==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
