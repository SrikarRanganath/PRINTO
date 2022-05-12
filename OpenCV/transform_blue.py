import argparse
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
incoming = [11, 11, 12, 13, 14, 16, 19, 21, 20, 21, 25, 22, 24, 25, 27, 28, 32, 34, 36, 40, 44, 51, 48, 52, 53, 55, 60, 63, 63, 65, 67, 71, 77, 71, 70, 70, 70, 69, 70, 70, 70, 71, 75, 82, 73, 74, 72, 74, 74, 75, 73, 71, 72, 75, 83]
reference = [0, 4, 9, 14, 18, 23, 28, 32, 37, 42, 47, 51, 56, 61, 65, 70, 75, 80, 84, 89, 94, 98, 103, 108, 113, 117, 122, 127, 131, 136, 141, 146, 150, 155, 160, 164, 169, 174, 178, 183, 188, 193, 197, 202, 207, 211, 216, 221, 226, 230, 235, 240, 244, 249, 254]
print("\nincoming = ",incoming,"\n")
print("\nreference = ",reference,"\n")
x, y = zip(*sorted(zip(incoming, reference)))
xpoints = np.array(x)
ypoints = np.array(y)
plt.plot(xpoints, ypoints)
plt.show()
def average(indices):
    sum = 0
    avg = 0
    for i in indices:
        sum+=reference[i]
    avg = sum/len(indices)
    return avg
in_array = []
out_array = []
for value in range (256):
    in_array.append(value)
    if value in incoming:
        indices = [i for i, x in enumerate(incoming) if x == value]
        print("corresponding occurances of ",value," are, ",list(reference[i] for i in indices))
        print("average look up value of ", value ,"is, ", average(indices),"\n")
        out_array.append(average(indices))
    else:
        out_array.append(-1)
        
print("\nincoming = ",in_array)
print("\nreference = ",out_array)
################################################################################################################################################
incoming = in_array
reference = out_array
start_index = 0
end_index = 0
current_index  = 0

def approximate(start_index , end_index):
    if end_index < 256 and start_index!=-300:
        n1 = reference[start_index]
        n2 = reference[end_index] 
        d1 = incoming[start_index]
        d2 = incoming[end_index] 
        step_size = (n2 - n1) / (d2 - d1)
        for i in range (start_index+1 , end_index):
            reference[i]=(reference[i-1] + step_size)
    elif end_index >= 256 and start_index!=-300:
        for i in range (start_index+1 , 256):
            reference[i]=255
    elif end_index <256 and start_index==-300:
        for i in range(0,end_index):
            reference[i]=reference[end_index]

i = 0
while( i < 255):
    if reference[i] == -1:
        start_index = i - 1
        end_index = i
        while(reference[end_index] == -1):
            end_index+=1        
            if end_index > 255:
                end_index = 300
                break
        i = end_index;
        if start_index < 0:
            start_index = -300
        #print("\n",start_index)
        #print("\n",end_index,"\n")
        approximate(start_index,end_index)
    i+=1
for i in range(256):
    reference[i] = round(reference[i])
print("\nreference = ",reference,"\n")

################################################################################################################################################

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
dim = (1100, 500) #width and height respectively
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
height=image.shape[0]
width =image.shape[1] # width of image
for i in range (height):
    for j in range (width):
        image[i,j,0] = reference[image[i,j,0]]
        #image[i,j,1] -= 5 
        #image[i,j,0] -= 7 
cv2.imshow("transformed",image)
reference = cv2.imread("/home/srikar/OpenCV/blue_palette.tif")
incoming = cv2.imread("/home/srikar/OpenCV/blue_palette_jig.tif")
incoming = cv2.resize(incoming, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("reference",reference)
cv2.imshow("incoming",incoming)
diff = cv2.subtract(image,reference)
"""for i in range(height):
    for j in range (width):
        #diff[i,j,2] =  math.exp(int(image[i,j,2] / 8))  
        diff[i,j,1] = math.exp(int(image[i,j,1] / 4))  
        diff[i,j,0] = math.exp(int(image[i,j,0] / 4))  """

cv2.imshow("difference_linear_interpolation",diff)
cv2.waitKey()




