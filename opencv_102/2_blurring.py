###############################################################################################################################
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Nikunj Lad
#
# This script explains various blurring techniques which can be used to pre-process an image. Blurring helps to reduce noise in
# an image. An image which is crisp and clear to human eye is actually noisy from a computer vision perspective. Blurring helps
# to reduce this noise by highlighting the important image features without worrying about minute details.
#
# 1. Average Blurring
# - This technique takes the average of all the pixels under the kernel area and replaces the central pixel with the average
# value.
# - This type of blurring is not aesthetically pleasing to human eye and it can seen un-natural. We never use this method
# though it helps to understand the concept of blurring
#
# 2. Gaussian Blurring
# - This technique uses weighted average of the pixels under the kernel area by giving importance to center pixel vs the border
# pixels. The weights follow a Gaussian distribution (bell curve) hence the name.
# - This type of blurring is more natural to human eye and is widely used in computer vision applications. Almost always we use
# Gaussian blurring unless there is a specific reason to use some other technique.
#
# 3. Median Blurring
# - This technique takes the median of all the pixels under the kernel area and replaces the central pixel with median value.
# - From a statistical point of view, median is more robust to outliers than average. It will return pixel value from the set
# of pixels under the kernel area. Hence it is very effective in removing 'salt and pepper' noise from an image.
# - This type of blurring is widely used in applications where salt and pepper noise is expected in the input images. But again
# this method will give unnatural look to the image and is not visually pleasing.
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
kernel_sizes = [(3, 3), (5, 5), (7, 7), (9, 9), (15, 15)]

# Apply Average Blurring
for (kx, ky) in kernel_sizes:
    blurred = cv2.blur(image, (kx, ky))
    cv2.imshow(f"Average Blurring: {kx}x{ky}", blurred)
    cv2.waitKey(0)

# Apply Gaussian Blurring
for (kx, ky) in kernel_sizes:
    # 0 indicates that the standard deviation in X and Y direction will be calculated based on kernel size by OpenCV itself
    # When doing Gaussian blurring, it is recommended to always set standard deviation to 0 and let OpenCV calculate it for you
    blurred = cv2.GaussianBlur(image, (kx, ky), 0)
    cv2.imshow(f"Gaussian Blurring: {kx}x{ky}", blurred)
    cv2.waitKey(0)

# Apply Median Blurring
# OpenCV only accepts single integer value for kernel size in median blurring as it always uses square kernels
for k in [3, 5, 7, 9, 15]:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median Blurring: {k}x{k}", blurred)
    cv2.waitKey(0)

# close all open windows and exit
cv2.destroyAllWindows()
sys.exit(0)