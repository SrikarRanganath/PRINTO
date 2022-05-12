import math
import PIL
import extcolors
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import gridspec
import cv2
import argparse

def study_image(image_path):
  
  img = Image.open(image_path)
  colors = extract_colors(img)
  color_palette = render_color_platte(colors)
  img = np.asarray(img)
  color_palette = np.asarray(color_palette)
  img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  
  color_palette = cv2.cvtColor(color_palette, cv2.COLOR_RGB2BGR)  
  cv2.imshow("image",img)
  cv2.imshow("color palette",color_palette)
  cv2.waitKey()
  #overlay_palette(img, color_palette)

def fetch_image(image_path):
  urllib.request.urlretrieve(image_path, "image")
  img = PIL.Image.open("image")
  return img

def extract_colors(img):
  tolerance = 5
  limit = 60
  colors, pixel_count = extcolors.extract_from_image(img, tolerance, limit)
  return colors

def render_color_platte(colors):
  size = 100
  columns = 11
  width = int(min(len(colors), columns) * size)
  height = int((math.floor(len(colors) / columns)) * size)
  result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
  canvas = ImageDraw.Draw(result)
  for idx, color in enumerate(colors):
      x = int((idx % columns) * size)
      y = int(math.floor(idx / columns) * size)
      canvas.rectangle([(x, y), (x + size - 1, y + size - 1)], fill=color[0])
  return result

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())
study_image(args["image"])

