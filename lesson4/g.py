import cv2
import numpy as np

read=cv2.imread("1bit.png")
reads=cv2.imread("2bit.png")
#bitwise and operator
ghj=cv2.bitwise_and(read,reads,mask=None)
cv2.imshow("yesyee",ghj)
cv2.waitKey(0)
#Bitwise or operator
ghj=cv2.bitwise_or(read,reads,mask=None)
cv2.imshow("yesyee",ghj)
cv2.waitKey(0)
#Bitwise xor operator
ghj=cv2.bitwise_xor(read,reads,mask=None)
cv2.imshow("yesyee",ghj)
cv2.waitKey(0)
#Bitwise xor operator
ghj=cv2.bitwise_not(read,mask=None)
ghjs=cv2.bitwise_not(reads,mask=None)
cv2.imshow("yesyee",ghj)
cv2.imshow("uguuds",ghjs)
cv2.waitKey(0)