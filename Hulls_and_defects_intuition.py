import cv2
import numpy as np
from time import sleep


im=cv2.imread('yash1.png')
cv2.imshow('imagesource',im)
cv2.waitKey(0)

imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow('imagegray',imgray)
cv2.waitKey(0)

ret,thresh1 = cv2.threshold(imgray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('thresholded',thresh1)
cv2.waitKey(0)

image,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#print contours[0][0]
#print contours[0][1]
#print contours[0][2]
#print contours[0][3]
#print contours[0][2][0][0]
#print contours[0][2][0][1]


#c=contours[0][2][0][0]
#b=contours[0][2][0][1]
#cv2.circle(im,(b,c),10,(0,0,255),-1)
#cv2.imshow('dot1',im)
#cv2.waitKey(0)


#########function source code
cnt = max(contours, key = lambda x: cv2.contourArea(x))
    
hull = cv2.convexHull(cnt)


x=hull.shape[0]  #x nnumber of points in the contour
y=hull.shape[1] # y dont know what it is actually
z=hull.shape[2] #z is used to define coordinates of the points in the contour

for i in range(0,x):
	c=hull[i][0][0]
	b=hull[i][0][1]

	cv2.circle(im,(c,b),5,(0,0,255),-1)
	cv2.imshow('dot1',im)
	cv2.waitKey(0)



hull2 = cv2.convexHull(cnt,returnPoints = False)
x=hull2.shape[0]  #x nnumber of points in the contour
y=hull2.shape[1] # y dont know what it is actually
print hull2
sleep(2)

defects = cv2.convexityDefects(cnt,hull2)

for i in range(defects.shape[0]):
	s,e,f,d = defects[i,0]

	start = tuple(cnt[s][0])
	cv2.circle(im,(start[0],start[1]),5,(0,255,255),-1)
	cv2.imshow('dot1',im)
	cv2.waitKey(0)

	end = tuple(cnt[e][0])
	cv2.circle(im,(end[0],end[1]),5,(255,0,0),-1)
	cv2.imshow('dot1',im)
	cv2.waitKey(0)

	far = tuple(cnt[f][0])
	cv2.circle(im,(far[0],far[1]),5,(0,0,0),-1)
	cv2.imshow('dot1',im)
	cv2.waitKey(0)
	
image,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = min(contours, key = lambda x: cv2.arcLength(x,True))

x,y,w,h = cv2.boundingRect(cnt)	
	
x=cnt.shape[0]  #x nnumber of points in the contour
y=cnt.shape[1] # y dont know what it is actually
z=cnt.shape[2] #z is used to define coordinates of the points in the contour

for i in range(0,x):
	c=cnt[i][0][0]
	b=cnt[i][0][1]

	cv2.circle(im,(c,b),5,(0,0,255),-1)
	cv2.imshow('dot1',im)
	cv2.waitKey(0)

#############################


#cnt = min(contours, key = lambda x: cv2.arcLength(x,True))

#x,y,w,h = cv2.boundingRect(cnt)





#im=cv2.drawContours(im, [cnt],0, (255,255,0),3)
#cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),0)

#cv2.imshow('im',im)
#cv2.waitKey(0)






