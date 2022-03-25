#from matplotlib import pyplot as plt
import argparse
import cv2

# j is for rows and i is for columns

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])

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
    avg_r = "{:.2f}".format(( r1 + r2 + r3 )/15)
    avg_g = "{:.2f}".format(( g1 + g2 + g3 )/15)
    avg_b = "{:.2f}".format(( b1 + b2 + b3 )/15)
    make_border(j,i,image)
    return tuple((avg_r,avg_g,avg_b))
    #return int(image[j,i,0])

def print_image_info(image):
    print("width: %d pixels" % (image.shape[1]))
    print("height: %d pixels" % (image.shape[0]))
    print("channels: %d" % (image.shape[2]))

print_image_info(image)
height=image.shape[0]
width =image.shape[1] # width of image
column_width = int(width / 1) #width of each column keep denom = 23 for cmyk full band image
mid_point = int(column_width / 2)

for i in range(mid_point,width,column_width): #This becomes columns
   print("\n")
   for j in range(5,height-13,13): # (ROWS) Leave some pixels(12.8) to get 255 buckets 
      print(average(j,i,image))

cv2.imshow("image",image)
cv2.imwrite("sampled_img1.jpg",image)
cv2.waitKey(0)





