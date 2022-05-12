# importing PIL Module
from PIL import Image
 
# open the original image
original_img = Image.open("/home/srikar/OpenCV/full_red_jig.tif")
 
 
# Flip the original image horizontally
horz_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)
horz_img.save("horizontal.png")
 
# close all our files object
original_img.close()
horz_img.close()
