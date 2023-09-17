"""
_summary_

This script shows how to crop an image. We will first create a sample numpy array with random numbers and understand cropping on the command line. Next, we will import a custom image and extract
ROI (regions of interest) using cropping

"""

__maintainer__ = "Nikunj Lad"

# import relevant libraries
import cv2, argparse, sys
import numpy as np


# create an image with numbers using numpy
I = np.arange(0, 25)  # create an array with numbers from  0 to 25
I = I.reshape((5,5))    # reshape the array of numbers in a 5x5 grid to represent an image
print(f"Numpy Image \n {I}")

#  array([[ 0,  1,  2,  3,  4],
#         [ 5,  6,  7,  8,  9],
#         [10, 11, 12, 13, 14],
#         [15, 16, 17, 18, 19],
#         [20, 21, 22, 23, 24]])

# cropping 4th and 5th row along with first 2 columns
crop = I[3:5, 0:2]
print(f"Crop of 4th and 5th row and first 2 columns \n {crop} \n")

# cropping out first 3 rows along with 4 columns starting 2nd column
crop = I[0:3, 1:5]
print(f"Crop of first 3 rows along with 4 columns starting 2nd column \n {crop} \n")

# cropping out only 3rd column from the image
crop = I[:, 2]
print(f"Crop of only 3rd column in the image \n {crop} \n")

# crop parts of an image starting 3rd row and 1st column in intervals of 2. Basically we want to crop elements at specific intervals given the start row and column
crop = I[2::2, ::2]
print(f"Crop image in intervals of 2 starting 3rd row and 1st column \n {crop} \n")


# parsing command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Input image to crop")
args = vars(ap.parse_args())

# read an image
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

head = image[10:75, 86:294]
cv2.imshow("Head of the bird", head)

bird = image[17:348, 85:491]
cv2.imshow("Only Bird", bird)

cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit(0)

