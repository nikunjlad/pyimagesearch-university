"""
Translate images i.e. shift them right, left, top, bottom or the combination of the 2 in the 2D plane

Translation makes use of a concept called warping. Given a set of co-ordinates (x1,y1), warping maps them to new co-ordinates (x2, y2)
The matrix used for translation is somewhat like this:
		T = [[1, 0, shiftX],
		     [0, 1, shiftY]]

In the above 2x3 matrix, the shiftX and shiftY parameters control how the image is translated in the 2D plane
1. -ve shiftX values: translate an image to the left in the 2D plane
2. +ve shiftX values: translate an image to the right in the 2D plane
3. -ve shiftY values: translate an image to the top in the 2D plane
4. +ve shiftY values: translate an image to the bottom in the 2D plane

A combination of above moves images in top-left, top-right, bottom-left, bottom-right locations or simply linearly across all 4 directions
"""

__maintainer__ = "Nikunj Lad"

# importing relevant libraries
import cv2, argparse, sys
import numpy as np

# parse command-line arguments
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image", type=str, default="troupial.jpg", help="path to input image")
args = vars(ag.parse_args())

# read the input image
image = cv2.imread(args["image"])
cv2.imshow("original", image)

# create a translational matrix to translate image to 25 pixels on the right and 50 pixels to the top
M = np.float32([[1, 0, 25], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted to the top-right", shifted)

# create another translational matrix to translate to 50 pixels to left and 90 pixels to the bottom
M = np.float32([[1, 0, -50], [0, 1, 90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted to the bottom-left", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit(0)
