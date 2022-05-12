import numpy as np
import cv2

width = 1100
height = 500

box_width = 100
box_height = 100

image = np.zeros((height,width,3), np.uint8)
mid_point_x = int((box_width-1) / 2)
mid_point_y = int((box_height-1) / 2)

blue = 0
for k in range (mid_point_y,height,100): #rows
    for l in range(mid_point_x,width,100): #columns
        print(np.uint8(blue))
        for i in range(-49,51):
            for j in range(-49,51):
                    image[(k + j) ,(l  + i)] = (blue,0,0)
        blue += 4.71
cv2.imshow("palette",image)
cv2.waitKey()
cv2.imwrite("blue_palette.tif",image)
