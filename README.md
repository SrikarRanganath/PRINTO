# PRINTO

all the codes and images are in folder named "files"

Take the full C band image from incoming and reference. 

Give these images as inputs to sampling.py

You get an array of averaged pixel values as output from sampling.py (Look into .txt files in this repo to see output of sampling.py)

take two arrays, one each from reference and incoming.

give these two arrays as inputs to lookup.py (giving input is changing the code in lookup.py)

You get 2 arrays( LOOK_in and LOOK_out) for one channel ( C )

take the two arrays and give them as inputs for LUT.py

output of the LUT.py will be a semi-transformed image(without interpolation) and you will also get a graph that interpolates the data

Next step is to find a way to use data from graph for interpolation

IGNORE convert.py FOR NOW

Figure1.jpg is the interpolation graph I got from LUT.py

