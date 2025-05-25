import cv2
import numpy as np
read=cv2.imread("image.jpg")
reads=cv2.imread("rgb.png")
#weighted addition
add=cv2.addWeighted(read,0.8,reads,0.6,0)

cv2.imshow("Pictures",add)
cv2.waitKey(0)

#weighted sub
add=cv2.subtract(read,reads)
cv2.imshow("Picturessssss",add)
cv2.waitKey(0)
#resizing image
read=cv2.imread("image.jpg")
store=cv2.resize(read,(600,800))
cv2.imshow("Picturessreressss",store)
cv2.waitKey(0)
#erosion effect
store=np.ones((5,5),np.uint8)
erroded=cv2.erode(read,store)

cv2.imshow("Pictures",erroded)
cv2.waitKey(0)

#bluring of an image
read=cv2.imread("image1.jpg")
cv2.imshow("Pictures",read)
cv2.waitKey(0)
#Gaussian blur
store=cv2.GaussianBlur(read,(7,7),0)
cv2.imshow("Pictures",store)
cv2.waitKey(0)

#median blur
store=cv2.medianBlur(read,5)
cv2.imshow("nfgfg",store)
cv2.waitKey(0)

#bilateral Filter
store=cv2.bilateralFilter(read,6,1,1)
cv2.imshow("Pictures",store)
cv2.waitKey(0)

#bordering an image
read=cv2.imread("image1.jpg")
border=cv2.copyMakeBorder(read,10,10,10,10,cv2.BORDER_CONSTANT,value=1)
cv2.imshow("bjhbuijb",border)
cv2.waitKey(0)

#reflecting border
border=cv2.copyMakeBorder(read,10,10,10,10,cv2.BORDER_REFLECT,value=1)
cv2.imshow("bjhbuijb",border)
cv2.waitKey(0)