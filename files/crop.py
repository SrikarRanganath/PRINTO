#!/usr/bin/python
import cv2
import numpy as np

def print_image_info(image):
    print("width: %d pixels" % (image.shape[1]))
    print("height: %d pixels" % (image.shape[0]))
    print("channels: %d" % (image.shape[2]))

image = cv2.imread('/home/srikar/OpenCV/CMYK_reference.tif')

image = cv2.resize(image,(622,254), interpolation= cv2.INTER_LINEAR)

print_image_info(image)
height = image.shape[0]
width = image.shape[1]
column_width = int(width / 23) #width of each column keep denom = 23 for cmyk full band image
mid_point = int(column_width / 2)
width_selector = 10

output_image = np.zeros((height-5,width_selector*2+1,3), np.uint8)
for column in range (mid_point + 0*column_width , 1*column_width , (column_width) ):
    for row in range (2,height-3):
        for pixel in range(-width_selector,width_selector+1):
            #temp.append(tuple(image[row , column+pixel]))
            out_column =  width_selector - pixel
            out_row = row - 2
            print(out_row,out_column)
            output_image[out_row,out_column,0] = image[row , column+pixel,0]
            output_image[out_row,out_column,1] = image[row , column+pixel,1]
            output_image[out_row,out_column,2] = image[row , column+pixel,2]

cv2.imshow("output",output_image)        
cv2.waitKey()
cv2.imwrite("C_reference_1.bmp",output_image)






