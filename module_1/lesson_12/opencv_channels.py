"""
_summary_

This script shows how to perform masking on images to segment out ROI (regions of interest) using bitwise operations. Essentially a binary mask is used with the region
we want to extract as foreground and everything else acting as background.
"""

__maintainer__ = "Nikunj Lad"

# import relevant libraries
import cv2, sys, argparse
import numpy as np

# parsing command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="../../data/images/opencv_logo.png", help="Path to input image")
args = vars(ap.parse_args())

# read the input image
image = cv2.imread(args["image"])

# split image into individual channels. Here each channel is gray scale image, where pixel value 0 means that color is absent (aka black region)
# and pixel value 255 means its present (aka white region)
# Note that for each color channel image, the region pertaining to that color would be white (denoting its present), while black would denote absent
(B, G, R) = cv2.split(image)
cv2.imshow("Original", image)
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
cv2.waitKey(0)

# merge all channels together
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Visualizing each channel as an image not just single channels
# earlier we saw each channel as 1-channel image. Now, we are going to fill the remaining channels are 0
# For instance, a Green image would have its B and R channel values as 0 while it display Green color for relevant parts of image having green color
# Same is true for other images
zeros = np.zeros(image.shape[:2], dtype=np.uint8)
red = cv2.merge([zeros, zeros, R])
green = cv2.merge([zeros, G, zeros])
blue = cv2.merge([B, zeros, zeros])
cv2.imshow("Original", image)
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()