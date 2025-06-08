import cv2
import os
from PIL import Image
os.chdir(r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4\lesson 7\images")
path=r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4\lesson 7\images"
avgh=0
width=0
numimages=len(os.listdir("."))
print(numimages)