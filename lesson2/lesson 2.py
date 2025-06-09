import cv2
import os
from PIL import Image
os.chdir(r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4\lesson 7\images")
path=r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4\lesson 7\images"
avgh=0
width=0
numimages=len(os.listdir("."))
print(numimages)
#finding mean width and height
for i in os.listdir("."):
    img=Image.open(os.path.join(path,i))
    widths,height=img.size
    width=width+widths
    avgh=avgh+height
width=width//5
avgh=avgh//5
print(avgh)
print(width)
for i in os.listdir("."):
    if i.endswith(".jpg") or i.endswith("jpeg"):
        img=Image.open(os.path.join(path,i))
        widths,height=img.size
        print(widths,height)
        #reszing 
        re=img.resize((width,avgh),Image.Resampling.LANCZOS)
        re.save(i,"JPEG",quality=100)
        print(img.filename.split('\\')[-1],"is resized")
#video generation
def vg():
    nameoffile="video.avi"
    os.chdir(r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4\lesson 7\images")
    imagess=[]
    for i in os.listdir("."):
        if i.endswith(".jpeg") or i.endswith("jpg"):
            imagess.append(i)
    print(imagess)
vg()
