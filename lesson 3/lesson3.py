import cv2
read=cv2.imread("pic1.jpg")
#drawing a line
start=(680,50)
end=(680,400)
color=(87,94,141)
thick=50
draw=cv2.line(read,start,end,color,thick)
cv2.imshow("dkl",draw)
cv2.waitKey(0)
#drawingg a rectangle
start=(0,10)
end=(710,450)
color=(87,94,141)
thick=-5789
draw=cv2.rectangle(read,start,end,color,thick)
cv2.imshow("dkl",draw)
cv2.waitKey(0)
cv2.destroyAllWindows()
#drawingg a cricle
reader=cv2.imread("pic1.jpg")
radius=75
var=(100,100)
color=(87,94,141)
thick=-6
draw=cv2.circle(reader,var,radius,color,thick)
cv2.imshow("dkl",draw)
cv2.waitKey(0)
#drawing text on the screen
readers=cv2.imread("pic2.jpg")
textsize=1
var=(100,100)
color=(86,34,75)
font=cv2.FONT_HERSHEY_TRIPLEX
thick=2
draw=cv2.putText(readers,'"No bird soars too high if he soars with his own wings"',var,font,textsize,color,thick,cv2.LINE_AA)
cv2.imshow("dkl",draw)
cv2.waitKey(0)
