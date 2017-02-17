import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)


black_img=np.zeros((450,450,3), np.uint8)
erase_img=np.zeros((450,450,3), np.uint8)



while(cap.isOpened()):

	#######show full image with rectangle
	ret, im = cap.read()
	im=cv2.flip(im,1)
	cv2.rectangle(im,(500,500),(50,50),(255,0,0),2)
	#cv2.imshow('imagesource',im)
	#cv2.waitKey(0)
	###########

	##### crop the rectangle###
	cropped_img = im[50:500, 50:500]
	#cv2.imshow(' cropped_img',cropped_img)
	#cv2.waitKey(2)
	######
	
	####Find and draw counters in the cropped image##
	imgray=cv2.cvtColor(cropped_img,cv2.COLOR_BGR2GRAY)
	#cv2.imshow('imagegray',imgray)
	#cv2.waitKey(2)
	ret,thresh1 = cv2.threshold(imgray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	cv2.imshow('thresholded',thresh1)
	cv2.waitKey(2)
	image,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	########
	
	####function source code
	cnt = max(contours, key = lambda x: cv2.contourArea(x))
    	hull = cv2.convexHull(cnt)
	
	x=hull.shape[0]  #x nnumber of points in the contour
	y=hull.shape[1] # y dont know what it is actually
	z=hull.shape[2] #z is used to define coordinates of the points in the contour
	
	corro_c=0
	minb=700
	
	for i in range(0,x):
		c=hull[i][0][0]
		b=hull[i][0][1]
	
		if b<minb:
			minb=b
			corro_c=c

	cv2.circle(cropped_img,(corro_c,minb),5,(0,255,255),-1)
	cv2.imshow('dot',cropped_img)
	cv2.waitKey(5)
	m=cv2.waitKey(5)
	cv2.circle(black_img,(corro_c,minb),5,(0,255,255),-1)
	cv2.imshow('dot1',black_img)
	k=cv2.waitKey(5)
	if (k==ord('e')) | (m==ord('e')):
		black_img=erase_img

	
