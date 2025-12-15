"""
Code to load image from disk and to save image to disk
"""

__maintainer__ = "Nikunj Lad"

# importing relevant libraries
import argparse
import cv2
from pathlib import Path
import sys

DATA_DIR = Path(__file__).parent.parent / "data"

# construct argument parser
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--input", default=DATA_DIR / "images/sun.jpg", help="path to input image")			# argument to load input images given its path
ag.add_argument("-o", "--output", default=Path.cwd() / "new_image.jpg", help="path to output image")		# argument to save input images to the given path
args = vars(ag.parse_args())				# create a dictionary of the parsed command line arguments to be loaded for later use

# load image from disk and grab spatial dimensions including width, height and channels
image = cv2.imread(args["input"])		# read input image
(h, w, c) = image.shape[:3]				# get shape of the image - height, width and channels

# display the image and print the image parameters
print(f"Width: {w} pixels")
print(f"Height: {h} pixels")
print(f"Channels: {c} channels")

# display image on screen
cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite(args["output"], image)		# write image to disk
sys.exit(0)								# throw a sys exit code of 0 on successful termination of code