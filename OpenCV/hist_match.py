# import the necessary packages
from skimage import exposure
import matplotlib.pyplot as plt
import argparse
import cv2
import time
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True,
	help="path to the input source image")
ap.add_argument("-r", "--reference", required=True,
	help="path to the input reference image")
args = vars(ap.parse_args())
# load the source and reference images
ts = time.time()
print("start time = ",ts)
print("[INFO] loading source and reference images...")
src = cv2.imread(args["source"])
ref = cv2.imread(args["reference"])



"""
scale_percent = 35 # percent of original size
width = int(ref.shape[1] * scale_percent / 100)
height = int(ref.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image"""

#height = int(ref.shape[0])
#width = int(ref.shape[1])
width  = 1100
height = 500
dim = (width, height)
ref = cv2.resize(ref,dim,interpolation = cv2.INTER_AREA )
src = cv2.resize(src,dim,interpolation = cv2.INTER_AREA )

# determine if we are performing multichannel histogram matching
# and then perform histogram matching itself
print("[INFO] performing histogram matching...")
multi = True if src.shape[-1] > 1 else False
matched = exposure.match_histograms(src, ref, multichannel=multi)



# show the output images
cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)
diff = cv2.subtract(ref,matched)
cv2.imshow("difference",diff)
ts = time.time()
print("end time = ",ts)
cv2.waitKey(0)
# construct a figure to display the histogram plots for each channel
# before and after histogram matching was applied
(fig, axs) =  plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
# loop over our source image, reference image, and output matched image
for (i, image) in enumerate((src, ref, matched)):
	# convert the image from BGR to RGB channel ordering
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# loop over the names of the channels in RGB order
	for (j, color) in enumerate(("red", "green", "blue")):
		# compute a histogram for the current channel and plot it
		(hist, bins) = exposure.histogram(image[..., j],
			source_range="dtype")
		axs[j, i].plot(bins, hist / hist.max())
		# compute the cumulative distribution function for the
		# current channel and plot it
		(cdf, bins) = exposure.cumulative_distribution(image[..., j])
		axs[j, i].plot(bins, cdf)
		# set the y-axis label of the current plot to be the name
		# of the current color channel
		axs[j, 0].set_ylabel(color)
# set the axes titles
axs[0, 0].set_title("Source")
axs[0, 1].set_title("Reference")
axs[0, 2].set_title("Matched")
#cv2.imwrite("reference.tif",ref)
#cv2.imwrite("matched.png",matched)
# display the output plots
plt.tight_layout()
plt.show()
