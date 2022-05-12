import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn import linear_model
import argparse
import cv2
incoming = [(13, 10, 16), (12, 9, 14), (12, 8, 13), (12, 8, 12), (14, 9, 13), (15, 9, 14), (15, 9, 14), (15, 9, 13), (15, 9, 14), (16, 9, 14), (18, 12, 17), (17, 11, 16), (15, 9, 13), (16, 9, 13), (16, 8, 12), (18, 9, 13), (19, 9, 13), (21, 9, 13), (22, 9, 12), (24, 9, 13), (27, 10, 14), (29, 12, 16), (28, 11, 16), (28, 9, 13), (30, 9, 12), (32, 9, 12), (34, 10, 13), (35, 10, 12), (38, 10, 12), (39, 10, 12), (42, 11, 13), (45, 12, 14), (48, 12, 16), (47, 12, 16), (47, 10, 13), (50, 10, 13), (52, 9, 12), (54, 10, 13), (56, 10, 13), (58, 10, 13), (60, 10, 13), (63, 11, 14), (66, 11, 15), (68, 12, 16), (65, 11, 14), (66, 10, 13), (68, 10, 13), (70, 9, 13), (72, 10, 14), (74, 11, 14), (75, 10, 14), (76, 10, 14), (78, 11, 15), (78, 11, 15), (79, 12, 16)]

"""incoming_photo_paper = [(60, 49, 45), (63, 50, 46), (64, 51, 47), (65, 52, 48), (67, 52, 47), (69, 53, 48), (68, 53, 48), (70, 53, 47), (72, 53, 47), (73, 54, 48), (73, 53, 47), (81, 51, 43), (84, 51, 44), (88, 50, 43), (89, 50, 43), (94, 50, 44), (100, 51, 46), (100, 51, 45), (104, 52, 46), (108, 51, 46), (109, 51, 46), (110, 51, 45), (122, 47, 41), (125, 47, 41), (132, 47, 41), (133, 47, 41), (136, 46, 41), (141, 47, 42), (142, 46, 42), (148, 46, 42), (151, 46, 43), (153, 45, 43), (153, 44, 42), (167, 31, 37), (171, 30, 37), (174, 30, 37), (174, 30, 37), (177, 31, 38), (181, 31, 38), (181, 31, 37), (184, 33, 36), (186, 35, 37), (186, 35, 37), (185, 35, 37), (193, 38, 35), (195, 40, 36), (198, 42, 39), (199, 43, 41), (201, 45, 44), (202, 46, 45), (202, 46, 45), (204, 47, 46), (203, 46, 45), (203, 46, 45), (200, 44, 44)]
"""


reference = [(0, 0, 0), (4, 0, 0), (9, 0, 0), (14, 0, 0), (18, 0, 0), (23, 0, 0), (28, 0, 0), (32, 0, 0), (37, 0, 0), (42, 0, 0), (47, 0, 0), (51, 0, 0), (56, 0, 0), (61, 0, 0), (65, 0, 0), (70, 0, 0), (75, 0, 0), (80, 0, 0), (84, 0, 0), (89, 0, 0), (94, 0, 0), (98, 0, 0), (103, 0, 0), (108, 0, 0), (113, 0, 0), (117, 0, 0), (122, 0, 0), (127, 0, 0), (131, 0, 0), (136, 0, 0), (141, 0, 0), (146, 0, 0), (150, 0, 0), (155, 0, 0), (160, 0, 0), (164, 0, 0), (169, 0, 0), (174, 0, 0), (178, 0, 0), (183, 0, 0), (188, 0, 0), (193, 0, 0), (197, 0, 0), (202, 0, 0), (207, 0, 0), (211, 0, 0), (216, 0, 0), (221, 0, 0), (226, 0, 0), (230, 0, 0), (235, 0, 0), (240, 0, 0), (244, 0, 0), (249, 0, 0), (254, 0, 0)]
red_x = [i[0] for i in incoming]
red_y = [i[0] for i in reference]
green_x = [i[1] for i in incoming]
green_y = [i[1] for i in reference]
blue_x = [i[2] for i in incoming]
blue_y = [i[2] for i in reference]
	
red_x, red_y = zip(*sorted(zip(red_x, red_y)))
green_x, green_y = zip(*sorted(zip(green_x, green_y)))
blue_x, blue_y = zip(*sorted(zip(blue_x, blue_y)))


"""
for i in range(len(red_x)):
	print(red_x[i])
for i in range(len(red_x)):
	print(red_y[i])
for i in range(len(red_x)):
	print(green_x[i])
for i in range(len(red_x)):
	print(green_y[i])
for i in range(len(red_x)):
	print(blue_x[i])
for i in range(len(red_x)):
	print(blue_y[i])              """

xpoints = np.array(red_x)
ypoints = np.array(red_y)
plt.plot(xpoints, ypoints)
plt.show()



df = pandas.read_csv("/home/srikar/Desktop/rgb3.csv")

X = df[['R_incoming', 'G_incoming', 'B_incoming']]
y = df['R_reference']

regr = linear_model.LinearRegression()
regr.fit(X.values, y)
red_x = df['R_incoming']
blue_x = df['G_incoming']
green_x = df['B_incoming']
red_y = df['R_reference']
print(regr.coef_," ",regr.intercept_)
coeff = regr.coef_
constant = regr.intercept_
for i in range(len(red_x)):
    print(red_y[i] - regr.predict([[red_x[i],green_x[i],blue_x[i]]]))
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])

#######################################################################
dim = (1100, 500)
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
########################################################################

height=image.shape[0]
width =image.shape[1] # width of image
cv2.imshow("incoming",image)  
for i in range (int(height)):
    for j in range (int(width)):
        new_red = regr.predict([[image[i,j,2],image[i,j,1],image[i,j,0]]])
        if(new_red < 0):
            new_red = 0
        if(new_red>255):
            new_red =255
        image[i,j,2] = new_red    
        image[i,j,0] = 0
        image[i,j,1] = 0
cv2.imshow("incoming_transformed",image)
reference = cv2.imread("/home/srikar/OpenCV/red_palette.tif")
cv2.imshow("reference", reference)
image = cv2.subtract(reference,image)
cv2.imshow("diff",image)
cv2.waitKey()


