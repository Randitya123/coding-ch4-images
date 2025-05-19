#importing libarary
import cv2
#varaible to read the picture
read=cv2.imread("image.jpg",cv2.IMREAD_COLOR)
#shows the picture
cv2.imshow("Lamine Yamal",read)
#makes the picture stay for a long time
cv2.waitKey(0)
#idk

#reading and displaying image in grey scale
import cv2
#varaible to read the picture
read=cv2.imread("image.jpg",0)
cv2.imshow("Lamine Yamal",read)
#makes the picture stay for a long time
cv2.waitKey(0)
#saving a image after editing
import os
store=r"C:\Users\KIKE\OneDrive\Desktop\Coding ch4"
os.chdir(store)
cv2.imwrite("blakcandwehiotee.jpg",read)
print("good")
read=cv2.imread("rgb.png",1)
#spliting imaghe in blue green and red
b,g,r=cv2.split(read)
cv2.imshow("OG",read)
cv2.waitKey(0)
cv2.imshow("blue",b)
cv2.waitKey(0)
cv2.imshow("green",g)
cv2.waitKey(0)
cv2.imshow("red",r)
cv2.waitKey(0)
