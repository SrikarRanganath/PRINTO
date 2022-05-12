import cv2
import numpy as np
import argparse
samples = []
def number_of_colors(image):
    col_ver = set() #empty set
    col_hor = set() #empty set
    height = image.shape[0]
    width = image.shape[1]
    safe_margin = 10 #ten pixels
    for i in range (height):
        col_ver.add(tuple((image[i , safe_margin])))
    for i in range (width):
        col_hor.add(tuple((image[safe_margin , i])))
    return ( len(col_hor), len(col_ver),len(col_hor) * len(col_ver))    
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
#image = cv2.imread("/home/srikar/OpenCV/color_palette.png")
dim = (1100, 500)
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("color palette",image)
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
print("width of palette is ", width)
print("height of palette is ", height)
print("number of channels in palette is ", channels)
print("number of colors in the palette = ",number_of_colors(image))
palette_info = number_of_colors(image)
#box_width = int(width / palette_info[0]) 
#box_height = int(height / palette_info[1])
box_width = 100
box_height = 100
print(box_width, " ", box_height )

mid_point_x = int((box_width-1) / 2)
mid_point_y = int((box_height-1) / 2)

for k in range (mid_point_y,height,100): #rows
    for l in range(mid_point_x,width,100): #columns
        sum_of_pixels = (0,0,0) 
        for i in range(-24,25):
            for j in range(-24,25):
                sum_of_pixels =  np.add(sum_of_pixels,image[(k + j) , (l + i)])
                if(abs(i) == 24 or abs(j) == 24):
                    image[(k + j) ,(l  + i)] = (0,255,0)
        average = tuple(round(pixel/(49*49)) for pixel in sum_of_pixels)
        average = average[::-1]
        print(average)
        samples.append(average)
print(samples)

red=list( i[0] for i in samples)
green=list( i[1] for i in samples)
blue=list( i[2] for i in samples)
print("Red = ",red)
print("Green = ",green)
print("Blue = ",blue)

##UNCOMMENT THIS TO PRINT EACH CHANNEL VALUES SEPERATELY
"""for i in samples:
    print(i[0])
print("########################################################")
for i in samples:
    print(i[1])
print("########################################################")
for i in samples:
    print(i[2])
"""
cv2.imshow("sampled", image)
cv2.waitKey()





