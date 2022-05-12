# This code is to show images 
# In the CLI, type "python3 show.py -i 'image_name_with_full_path' "
import argparse
import cv2
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])


cv2.imwrite("M_reference.bmp",image)
cv2.imshow("Image",image)
cv2.waitKey(0)
