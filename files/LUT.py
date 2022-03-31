import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# data to be plotted

image1=cv2.imread('/home/srikar/OpenCV/CMYK_reference.jpg') #reference
image2=cv2.imread('/home/srikar/OpenCV/CMYK_incoming.jpg') #incoming



height=image1.shape[0]
width =image1.shape[1]
print(height," ",width)
down_points = (width,height)
image2 = cv2.resize(image2,down_points,interpolation = cv2.INTER_LINEAR)

image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)


reference =[5, 9, 9, 9, 14, 15, 20, 20, 20, 20, 22, 24, 28, 30, 39, 41, 44, 54, 54, 66, 74, 73, 83, 86, 91, 91, 98, 98, 102, 106, 107, 106, 109, 112, 112, 117, 117, 119, 117, 119, 121, 126, 127, 127, 127, 131, 131, 139, 142, 137, 139, 137, 147, 147, 153, 153, 153, 157, 158, 158, 158, 158, 163, 163, 165, 163, 163, 164, 168, 168, 168, 168, 173, 173, 173, 173, 178, 183, 178, 188, 178, 181, 182, 183, 185, 183, 185, 188, 194, 193, 193, 193, 198, 198, 198, 204, 204, 204, 209, 209, 209, 214, 213, 214, 214, 219, 219, 219, 220, 219, 224, 224, 224, 224, 229, 229, 233, 229, 234, 234, 236, 240, 242, 247, 249, 253, 255]


incoming = [0, 1, 2, 3, 5, 6, 13, 15, 16, 17, 20, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 43, 44, 45, 46, 50, 51, 54, 57, 58, 59, 60, 61, 64, 66, 67, 69, 70, 76, 78, 79, 80, 82, 83, 84, 90, 91, 96, 98, 99, 102, 103, 105, 110, 111, 114, 118, 119, 120, 121, 124, 126, 129, 130, 132, 134, 138, 139, 140, 149, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 164, 165, 166, 169, 173, 176, 177, 186, 189, 190, 197, 200, 202, 208, 210, 212, 213, 217, 219, 221, 222, 223, 229, 230, 231, 233, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 249, 250, 251]


x = incoming
y = reference
 
# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color ="red")
plt.show()

cv2.imshow("reference_before_transform",image1)
cv2.imshow("incoming",image2)
for i in range(width):
    for j in range(height):
        if image2[j,i] in incoming:
            index = incoming.index(image2[j,i])
            image2[j,i] = reference[index]

cv2.imshow("after_transform",image2)
cv2.waitKey()
