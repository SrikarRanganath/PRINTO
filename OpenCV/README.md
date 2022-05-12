1) color_palette.py will create a color palette from a given image. 
It will take any given image and searches for most occuring colors in that.
You can set number of colors you want and also the threshold value for considering two colors as different
reduce it (but do no make it 0) for getting more colors(also increasse the palette size)
each color will be of dimensions 100x100 pixels

2) palette_maker.py will create a 1100x500 palette. 
Inside this you can select the size of each box and intensity difference between adjacent blocks.
You will find 55 colors inside the palette

3) Take a print of generated palette and give the scanned and original image as arguments for box_sampling.py
This will give you 55 samples of (r,g,b)

4) Take these channels independently each at a time and put the array in transform_red _green or _blue.py files.

