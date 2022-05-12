#from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

# j is for rows and i is for columns

samples = []


def make_border(j,i,image):
    for k in range (-2,3):
        image[j-1,i-k] = 255
        image[j+1,i-k] = 255
    image[j,i-2] = 255
    image[j,i+2] = 255
    
def average(j,i,image):
    for column in range (-5:6):
    
    i1 =int(image[j-1,i-2])+int(image[j-1,i-1])+int(image[j-1,i])+int(image[j-1,i+1])+int(image[j-1,i+2]) 
    i2 =int(image[j-0,i-2])+int(image[j-0,i-1])+int(image[j-0,i])+int(image[j-0,i+1])+int(image[j-0,i+2]) 
    i3 =int(image[j+1,i-2])+int(image[j+1,i-1])+int(image[j+1,i])+int(image[j+1,i+1])+int(image[j+1,i+2]) 

    avg_i = (int(i1)+int(i2)+int(i3))/15
    make_border(j,i,image)
    avg_i = np.uint8(avg_i)
    #print(avg_i)
    samples.append(avg_i)

def print_image_info(image):
    print("width: %d pixels" % (image.shape[1]))
    print("height: %d pixels" % (image.shape[0]))

################################################    DRIVER CODE    ####################################

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #convert the image to  gray scale
print_image_info(image)
height=image.shape[0]
width =image.shape[1] # width of image
column_width = int(width / 1) #width of each column keep denom = 23 for cmyk full band image
mid_point = int(column_width / 2)

for i in range(mid_point,width,column_width): #This becomes columns
  print("\n")
  for j in range(5,height-5,5): # (ROWS) Leave some pixels(5.5) to get 255 buckets after each bucket
     average(j,i,image)

for pixel in samples:
	print(pixel)
print(samples)	

cv2.imshow("image",image)
cv2.imwrite("sampled_img1.jpg",image)
cv2.waitKey(0)

################################ CHECK MISSING VALUES #################################################



"""
missing_count = 0
print("\n",RED,"\n")
print(" \n RED MISSING LIST")
for i in range(256):
    if i in RED:
        continue
    else:
        print(i)
        missing_count +=1
print("\n")
print("number of missed values are : ",missing_count,"\n")        


missing_count = 0
print("\n",GREEN,"\n")
print(" \n GREEN MISSING LIST")
for i in range(256):
    if i in GREEN:
        continue
    else:
        print(i)
        missing_count +=1
print("\n")
print("number of missed values are : ",missing_count,"\n")        


missing_count = 0
print("\n",BLUE,"\n")
print(" \n BLUE MISSING LIST")
for i in range(256):
    if i in BLUE:
        continue
    else:
        print(i)
        missing_count +=1
print("\n")
print("number of missed values are : ",missing_count,"\n")        """

