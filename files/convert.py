import argparse
import cv2
import numpy as np


reference_R =[0, 4, 6, 11, 14, 16, 17, 21, 26, 28, 30, 31, 32, 36, 38, 41, 44, 46, 50, 51, 56, 57, 58, 62, 64, 67, 72, 76, 77, 80, 82, 84, 87, 91, 92, 95, 97, 98, 99, 102, 107, 108, 111, 113, 118, 121, 123, 127, 128, 130, 132, 133, 137, 138, 140, 143, 147, 148, 149, 151, 152, 153, 157, 159, 164, 166, 169, 173, 174, 176, 177, 178, 179, 181, 183, 184, 185, 189, 192, 194, 199, 202, 204, 210, 214, 215, 219, 220, 223, 225, 227, 230, 232, 235, 239, 240, 243, 244, 245, 248, 250] 

incoming_R =[3, 3, 5, 6, 8, 8, 9, 9, 13, 11, 13, 19, 23, 26, 28, 33, 38, 43, 54, 54, 67, 64, 70, 77, 89, 84, 99, 84, 91, 95, 100, 108, 112, 119, 123, 143, 132, 224, 143, 144, 151, 154, 156, 162, 171, 169, 170, 174, 176, 173, 168, 186, 187, 189, 193, 193, 199, 200, 208, 86, 202, 203, 207, 211, 213, 210, 213, 215, 216, 218, 216, 225, 219, 13, 219, 218, 218, 219, 220, 221, 222, 224, 223, 224, 224, 225, 226, 225, 226, 228, 230, 229, 231, 234, 234, 245, 254, 246, 250, 250, 254] 


reference_G =  [250, 250, 218, 245, 248, 255]

incoming_G = [251, 250, 251, 249, 254, 255]

reference_B = [255, 218, 245, 248, 249, 255]

incoming_B = [253, 254, 253, 254, 251, 245]


image1=cv2.imread('/home/srikar/OpenCV/Canvera_CMYK_Linearization.tif') #reference

image2=cv2.imread('/home/srikar/OpenCV/CMYK.jpg') #incoming

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
for i in range(0,int(width/3)): #This becomes columns
    for j in range(0,height):
        red = image1[j,i,2]
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
            image1[j,i,0] = incoming_B[index]



cv2.imshow("incoming_image",image2)
cv2.imwrite("incoming_image.bmp",image2)
cv2.imshow("reference_image_transformed",image1)
cv2.imwrite("reference_image_transformed.bmp",image1)
cv2.waitKey(0)


