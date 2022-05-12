""" 
this code is used to sample images. the kernel that I used for sampling is 3 X 5. 
3X5 matrix will have  15 values. Find average of those 15 values.
I appplied this code on incoming and reference CYAN_full bands.
j is for rows and i is for columns

usage : python3 sampling.py -i /home/srikar/image.extension > output.txt
check the output in output.txt file
"""

#from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

#RED = []
#GREEN = []
#BLUE =[] 
cmyk_samples = []

#This is RGB to CMYK conversion function
def rgb_to_cmyk (avg_red, avg_green, avg_blue):
   r1 = avg_red / 255
   g1 = avg_green / 255
   b1 = avg_blue / 255
   k =1 - max(r1,g1,b1)
   c = ((1-r1)-k)/(1-k)
   m = ((1-g1)-k)/(1-k)
   y = ((1-b1)-k)/(1-k)
   cmyk_tuple = (int(c*255),int(m*255),int(y*255),int(k*255))
   cmyk_samples.append(cmyk_tuple)
   #print(cmyk_tuple)

#This function will create green coloured border around the averaged_sampled_area
#Call this function only after taking the average as the borders are also included in averaging
def make_border(j,i,image):
    for k in range (-2,3):
        image[j-1,i-k] = (0,255,0)
        image[j+1,i-k] = (0,255,0)
    image[j,i-2] = (0,255,0)
    image[j,i+2] = (0,255,0)
    
def average(j,i,image):
    r1 =int(image[j-1,i-2,2])+int(image[j-1,i-1,2])+int(image[j-1,i,2])+int(image[j-1,i+1,2])+int(image[j-1,i+2,2]) 
    r2 =int(image[j-0,i-2,2])+int(image[j-0,i-1,2])+int(image[j-0,i,2])+int(image[j-0,i+1,2])+int(image[j-0,i+2,2]) 
    r3 =int(image[j+1,i-2,2])+int(image[j+1,i-1,2])+int(image[j+1,i,2])+int(image[j+1,i+1,2])+int(image[j+1,i+2,2]) 
    g1 =int(image[j-1,i-2,1])+int(image[j-1,i-1,1])+int(image[j-1,i,1])+int(image[j-1,i+1,1])+int(image[j-1,i+2,1]) 
    g2 =int(image[j-0,i-2,1])+int(image[j-0,i-1,1])+int(image[j-0,i,1])+int(image[j-0,i+1,1])+int(image[j-0,i+2,1]) 
    g3 =int(image[j+1,i-2,1])+int(image[j+1,i-1,1])+int(image[j+1,i,1])+int(image[j+1,i+1,1])+int(image[j+1,i+2,1]) 
    b1 =int(image[j-1,i-2,0])+int(image[j-1,i-1,0])+int(image[j-1,i,0])+int(image[j-1,i+1,0])+int(image[j-1,i+2,0]) 
    b2 =int(image[j-0,i-2,0])+int(image[j-0,i-1,0])+int(image[j-0,i,0])+int(image[j-0,i+1,0])+int(image[j-0,i+2,0]) 
    b3 =int(image[j+1,i-2,0])+int(image[j+1,i-1,0])+int(image[j+1,i,0])+int(image[j+1,i+1,0])+int(image[j+1,i+2,0]) 

    #b1,g1,r1 = (image[j-2,i-2]+image[j-2,i-1]+image[j-2,i]+image[j-2,i+1]+image[j-2,i+2])  
    avg_r = (int(r1)+int(r2)+int(r3))/15
    avg_g = (int(g1)+int(g2)+int(g3))/15
    avg_b = (int(b1)+int(b2)+int(b3))/15
    make_border(j,i,image)
    avg_r = np.uint8(avg_r)
    avg_g = np.uint8(avg_g)
    avg_b = np.uint8(avg_b)
    rgb_to_cmyk(avg_r, avg_g, avg_b)
    #pixel = tuple((avg_r, avg_g, avg_b))
    #RED.append(avg_r)
    #GREEN.append(avg_g)
    #BLUE.append(avg_b)
    #return  pixel
    #return int(image[j,i,0])
	
#This function is used to display the image properties(width , height, number of channels)
def print_image_info(image):
    print("width: %d pixels" % (image.shape[1]))
    print("height: %d pixels" % (image.shape[0]))
    print("channels: %d" % (image.shape[2]))

################################################    DRIVER CODE    ####################################

# Following block is used take input image name as argument from CLI
######################################################################################################
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
######################################################################################################

print_image_info(image)
height=image.shape[0]
width =image.shape[1] # width of image
column_width = int(width / 1) #width of each column keep denom = 23 for cmyk full band image
mid_point = int(column_width / 2)

for i in range(mid_point,width,column_width): #This becomes columns 
  print("\n")
  for j in range(5,height-5,5): # (ROWS) Leave some pixels(5) to get 255 buckets after each bucket
     #print(average(j,i,image))
     average(j,i,image)
for pixel in cmyk_samples:
	print(pixel)
print(cmyk_samples)

cv2.imshow("image",image)
cv2.imwrite("sampled_img1.jpg",image) #change the name as per the input image
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
