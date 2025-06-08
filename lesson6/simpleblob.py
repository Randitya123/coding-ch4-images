import cv2
import numpy as np

dt=cv2.imread("circle.png",0)
rules=cv2.SimpleBlobDetector_Params()
rules.filterByArea=True
rules.minArea=35
rules.filterByCircularity=True
rules.minCircularity=0.9
rules.filterByConvexity=True
rules.minConvexity=0.2
rules.filterByInertia=True
rules.minInertiaRatio=0.01
#creating a detector with paramenters
det=cv2.SimpleBlobDetector_create(rules)
keypoints=det.detect(dt)
#drawuign blocks on the images as red cricles
draws=np.zeros((1,1))
blobs=cv2.drawKeypoints(dt,keypoints,draws,(0,0,150),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numblobs="Blobs:"+str(len(keypoints))
cv2.putText(blobs,numblobs,(100,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(56,86,90),2)
cv2.imshow("title",blobs)
cv2.waitKey(0)
