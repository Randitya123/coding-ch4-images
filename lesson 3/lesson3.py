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
radius=75
var=(100,100)
color=(87,94,141)
thick=-6
draws=cv2.circle(read,var,radius,color,thick)
cv2.imshow("dkl",draws)
cv2.waitKey(0)
