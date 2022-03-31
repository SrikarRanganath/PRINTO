"""
This code is used to convert RGB image into C, M, Y, K, CMYK and grayscale
Don't forget to change the output file name in imwrite()

usage : python3 rgb_cmyk.py -i '/home/srikar/image.jpg'

"""
#!/usr/bin/python

import numpy as np
#import matplotlib.pyplot as plt
import cv2
import argparse

# Import image
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())
img=cv2.imread(args["image"])


# Create float
bgr = img.astype(float)/255.

# Extract channels
with np.errstate(invalid='ignore', divide='ignore'):
	K = 1 - np.max(bgr, axis=2)
	C = (1-bgr[...,2] - K)/(1-K)
	M = (1-bgr[...,1] - K)/(1-K)
	Y = (1-bgr[...,0] - K)/(1-K)

# Convert the input BGR image to CMYK colorspace
CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)

# Split CMYK channels
C, M, Y, K = cv2.split(CMYK)

np.isfinite(C).all()
np.isfinite(M).all()
np.isfinite(K).all()
np.isfinite(Y).all()
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', img)

cv2.imshow('Grayscale', gray_image)

cv2.imshow('cyan', C)

cv2.imshow('magenta', M)

cv2.imshow('yellow', Y)

cv2.imshow('key', K)

cv2.imshow('cmyk', CMYK)


cv2.waitKey(0)
# Save channels
cv2.imwrite('/home/srikar/OpenCV/C_cc.jpg', C)
cv2.imwrite('/home/srikar/OpenCV/M_cc.jpg', M)
cv2.imwrite('/home/srikar/OpenCV/Y_cc.jpg', Y)
cv2.imwrite('/home/srikar/OpenCV/K_cc.jpg', K)
cv2.imwrite('/home/srikar/OpenCV/CMYK_cc.jpg',CMYK)
