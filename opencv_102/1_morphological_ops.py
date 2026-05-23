###############################################################################################################################
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Nikunj Lad
#
# This script explains morphological operations which can be used to pre-process an image.
# 1. Erosion
# - This operation removes information from the image. More specifically, the foreground objects in the image shrink in size.
# - It is useful for removing small noise or small objects from the image.
# - This operation can be used in places like disconnecting touching objects or overlapping objects to analyze them separately.
#
# 2. Dilation
# - This operation adds information to the image. More specifically, the foreground objects in the image grow in size.
# - This operation is used after erosion to restore the size of the objects that were eroded.
# - Since erosion removes noise, the objects shrink as a side-effect. Dilation helps to restore original images.
#
# 3. Opening
# - Opening is an erosion followed by a dilation. It is used to remove noise from the image.
# - You can apply custom kernels to opening to remove noise of varying degrees of intensity in the image.
# - If the opening operation causes all noise to be removed, but image to be erroded, you can explicitly dilate later.
#
# 4. Closing
# - Closing is a dilation followed by an erosion. It is used to remove noise from the image.
# - You can apply custom kernels to closing to remove noise of varying degrees of intensity in the image.
#
# 5. Morphological Gradient
# - This operation is the difference between dilation and erosion of an image.
# - This operation is used to find the outline of the objects in the image.
# - This operation is useful when we need to find boundary of the foreground and background objects, edge detection, etc.
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
ap.add_argument("-i", "--image", type=str, default=DATA_DIR / "images/pyimagesearch_logo.png", help="Path to input image")
args = vars(ap.parse_args())

# read the input image
image = cv2.imread(args["image"])

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)

# Perform Erosion Operation on the image
for i in range(0, 3):
    erroded_image = cv2.erode(gray_image.copy(), None, iterations=i+1)
    cv2.imshow(f"Erroded image {i+1} times", erroded_image)
    cv2.waitKey(0)

# close open windows and clear screen
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)

# Perform Dilation Operation on the image
for i in range(0, 3):
    dilated_image = cv2.dilate(gray_image.copy(), None, iterations=i+1)
    cv2.imshow(f"Dilated image {i+1} times", dilated_image)
    cv2.waitKey(0)

# close open windows and clear screen
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)

# Perform Opening Operation on the image
kernel_sizes = [(3,3), (5,5), (7,7)]

for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opened_image = cv2.morphologyEx(gray_image.copy(), cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opened image with kernel size {kernel_size}", opened_image)
    cv2.waitKey(0)

# close open windows and clear screen
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)

# Perform Closing Operation on the image
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closed_image = cv2.morphologyEx(gray_image.copy(), cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Closed image with kernel size {kernel_size}", closed_image)
    cv2.waitKey(0)

# close open windows and clear screen
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)

# Perform Morphological Gradient operation on an image
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    gradient_image = cv2.morphologyEx(gray_image.copy(), cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(f"Gradient image with kernel size {kernel_size}", gradient_image)
    cv2.waitKey(0)

# close open windows and clear screen
cv2.destroyAllWindows()
sys.exit(0)
