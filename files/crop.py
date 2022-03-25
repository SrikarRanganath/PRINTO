"""#!/usr/bin/env python
BASE_PATH = '/home/srikar/1'
FILE_EXTENSION = '.bmp'


for idx, img in enumerate(gimp.image_list()):
	layer = img.layers[0]
	filename = BASE_PATH + str(idx) + FILE_EXTENSION
	gimp.pdb.gimp_by_color_select(layer, 'white', 12, 0, TRUE, 0, 0, 0)
	gimp.pdb.gimp_edit_clear(layer)
	gimp.pdb.plug_in_autocrop(img, layer)
	gimp.pdb.gimp_file_save(img, layer, filename, filename)"""


from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np


image = img_as_float(io.imread('resize_1.jpg'))

# Select all pixels almost equal to white
# (almost, because there are some edge effects in jpegs
# so the boundaries may not be exactly white)
white = np.array([1, 1, 1])
mask = np.abs(image - white).sum(axis=2) < 0.05

# Find the bounding box of those pixels
coords = np.array(np.nonzero(~mask))
top_left = np.min(coords, axis=1)
bottom_right = np.max(coords, axis=1)

out = image[top_left[0]:bottom_right[0],
            top_left[1]:bottom_right[1]]
out.savefig('ref_crop.png')
plt.imshow(out)
plt.show()
