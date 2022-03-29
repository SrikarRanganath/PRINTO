#!/usr/bin/python

import numpy as np
#import matplotlib.pyplot as plt
import cv2

# Import image
img = cv2.imread('/home/srikar/OpenCV/Canvera_CMYK_Linearization.tif', cv2.IMREAD_UNCHANGED)

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
cv2.imwrite('/home/srikar/OpenCV/reference_in_CMYK/C_cc.jpg', C)
cv2.imwrite('/home/srikar/OpenCV/reference_in_CMYK/M_cc.jpg', M)
cv2.imwrite('/home/srikar/OpenCV/reference_in_CMYK/Y_cc.jpg', Y)
cv2.imwrite('/home/srikar/OpenCV/reference_in_CMYK/K_cc.jpg', K)
cv2.imwrite('/home/srikar/OpenCV/reference_in_CMYK/CMYK_cc.jpg',CMYK)
