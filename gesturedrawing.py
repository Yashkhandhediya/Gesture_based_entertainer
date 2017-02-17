import cv2
import numpy as np
import math
from time import sleep

cap = cv2.VideoCapture(0)


black_img=np.zeros((480,640,3), np.uint8)
erase_img=np.zeros((480,640,3), np.uint8)



while(cap.isOpened()):

	#######show full image with rectangle
	ret, im = cap.read()
	im=cv2.flip(im,1)
	#cv2.rectangle(im,(500,500),(50,50),(255,0,0),2)
	#cv2.imshow('imagesource',im)
	#cv2.waitKey(0)
	###########

	##### crop the rectangle###
	cropped_img = im
	#cv2.imshow(' cropped_img',cropped_img)
	#cv2.waitKey(2)
	######
