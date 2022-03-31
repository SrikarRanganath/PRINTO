import argparse
import cv2
import numpy as np


reference_R =

incoming_R = 

reference_G =  

incoming_G =

reference_B =  

incoming_B = 


image1=cv2.imread('/home/srikar/OpenCV/CMYK_reference.tif') #reference

image2=cv2.imread('/home/srikar/OpenCV/incoming.bmp') #incoming

height=image1.shape[0]
width =image1.shape[1]
print(height," ",width)
down_points = (width,height)

"""image1[:,:,0] = 0
image1[:,:,1] = 0
image2[:,:,0] = 0
image2[:,:,1] = 0"""

image2 = cv2.resize(image2,down_points,interpolation = cv2.INTER_LINEAR)
cv2.imwrite("reference_image.bmp",image1)
cv2.imshow("reference image",image1)

def tuples_are_equal(tuple1 , tuple2):
	for i in range(0,len(tuple1)):
		if(abs(tuple1[i]-tuple2[i])>4):
			return False
	return True		
			
for column in range(0,int(width)): #This becomes columns
	for row in range(0,height):
		for index in range(0,len(incoming_R)):
			pixel_value = tuple((reference_R[index],reference_G[index],reference_B[index]))
			if(tuples_are_equal(pixel_value,image1[row,column])):
				print(pixel_value," ",image1[row,column])
				image1[row,column] = tuple((incoming_R[index],incoming_G[index],incoming_B[index]))
       	  
       
       
""" red = image1[j,i,2]
 if red in reference_R:
     index = reference_R.index(red)
            image1[j,i,2] = incoming_R[index]
        green = image1[j,i,1]
        if green in reference_G:
            index = reference_G.index(green)
            image1[j,i,1] = incoming_G[index]
        blue = image1[j,i,0]
        if blue in reference_B:
            index = reference_B.index(blue)
            image1[j,i,0] =  incoming_B[index]"""



cv2.imshow("incoming_image",image2)
#cv2.imwrite("incoming_image.bmp",image2)
cv2.imshow("reference_image_transformed",image1)
#cv2.imwrite("reference_image_transformed.bmp",image1)
cv2.waitKey(0)


