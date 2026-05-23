###############################################################################################################################
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Nikunj Lad
#
# This script explains how to use bilateral filtering for edge-preserving based image smoothing using blurring.
# Bilateral filtering is a non-linear, edge-preserving, and noise-reducing smoothing filter for images.
# Unlike usual blurring techniques, bilateral filtering considers both spatial proximity and pixel intensity differences.
# The first Gaussian function considering spatial proximity ensures that only nearby pixels are considered for blurring.
# The second Gaussian function considering pixel intensity differences ensures that only pixels with similar intensity values
# are considered for blurring. This dual consideration helps in preserving edges while effectively reducing noise.
#
# If pixels in neighborhood have same intensity values, then they are belonging to same region but if their intensity values
# vary then they may have an edge between them. In short, blur the details within a region of similar intensity (like say a sky
# or walls of a building), but do not blur across edges where intensity can change significantly.
#
# The only downside of bilateral filtering is that it is computationally expensive compared to other blurring techniques and
# hence it is slower. Below are parameters for bilateral filering:
# 1. Diameter - The pixel neighborhood to be considered for blurring. Instead of being a square region its circular. Its like a
# a kernel_size parameter in other blurring techniques. Larger the diameter, more pixels used for computing the blur.
#
# 2. SigmaColor - This is the standard deviation for the color (intensity) space. A larger value of sigmaColor means that more
# colors in the neighborhood will be considered for blur computation. If we set this value to be too large compared to diameter
# then it will consider pixels which are far away in intensity values and hence it will not preserve edges well.
#
# 3. SigmaSpace - This is the standard deviation for the coordinate space. A larger value of sigmaSpace means that pixels far
# away from the central pixel will influence the blurring calculation. If we set this value to be too large compared to diameter
# then it will consider pixels which are far away in spatial terms and hence it will not preserve edges well.
#
###############################################################################################################################

__maintainer__ = 'Nikunj Lad'

# Import necessary libraries
import argparse
import cv2
from pathlib import Path
import sys

DATA_DIR = Path(__file__).parent.parent / "data"

# parsing command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=DATA_DIR / "images/troupial.jpg", help="Path to input image")
args = vars(ap.parse_args())

# read the input image
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

diameters = [11, 13, 15, 17, 19]
sigma_colors = [21, 31, 41, 51, 61]
sigma_spaces = [7, 14, 21, 28, 35]

# Apply Bilateral Filtering - keeping diameter and sigmaColor constant and varying sigmaSpace
# Diameter = 15, SigmaColor = 41
for sigma_space in sigma_spaces:
    blurred = cv2.bilateralFilter(image, 15, 41, sigma_space)
    cv2.imshow(f"Bilateral Filtering: Diameter=15, SigmaColor=41, SigmaSpace={sigma_space}", blurred)
    cv2.waitKey(0)

# destory windows and clear screen
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)

# Apply Bilateral Filtering - keeping diameter and sigmaSpace constant and varying sigmaColor
# Diameter = 15, SigmaSpace = 21
for sigma_color in sigma_colors:
    blurred = cv2.bilateralFilter(image, 15, sigma_color, 21)
    cv2.imshow(f"Bilateral Filtering: Diameter=15, SigmaColor={sigma_color}, SigmaSpace=21", blurred)
    cv2.waitKey(0)

# destory windows and clear screen
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)

# Apply Bilateral Filtering - keeping SigmaColor and sigmaSpace constant and varying diameter
# SigmaColor = 41, SigmaSpace = 21
for diameter in diameters:
    blurred = cv2.bilateralFilter(image, diameter, 41, 21)
    cv2.imshow(f"Bilateral Filtering: Diameter={diameter}, SigmaColor=41, SigmaSpace=21", blurred)
    cv2.waitKey(0)

# destory windows and clear screen
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)

# close all open windows and exit
cv2.destroyAllWindows()
sys.exit(0)