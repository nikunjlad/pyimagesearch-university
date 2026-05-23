###############################################################################################################################
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Nikunj Lad
#
# This script explains specialized morphological operations like Top-Hat (White Hat) and Black Hat.
# 1. Top-Hat (White Hat)
# - This operation is a difference between the input image and its opening.
# - This operation highlights the bright features in an image on a dark background.
# - For instance, this can be used in OCR applications like finding license plates (white in color), over dark color cars.
#
# 2. Black Hat
# - This operation is a difference between the closing of the input image and the input image itself.
# - This operation highlights the dark features in an image on a bright background.
# - For example, this can be used in OCR applications like finding text (black in color), over a bright background like paper.
#
# Above specialized morphological operations can save us the trouble of complex Deep learning techniques.
# These are only to be used in controlled environments where the input images are in deterministic conditions.
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
ap.add_argument("-i", "--image", type=str, default=DATA_DIR / "images/car.png", help="Path to input image")
args = vars(ap.parse_args())

# read the input image
image = cv2.imread(args["image"])

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the kernel size for morphological operation
kernel_size = (13, 5)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

# Perform Top-Hat (White Hat) operation
top_hat = cv2.morphologyEx(gray_image.copy(), cv2.MORPH_TOPHAT, kernel)

# Perform Black Hat operation
back_hat = cv2.morphologyEx(gray_image.copy(), cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Top-Hat (White Hat) Operation", top_hat)
cv2.imshow("Black Hat Operation", back_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit(0)