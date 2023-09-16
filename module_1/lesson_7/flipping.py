"""
_summary_

This script shows how to flip an image. Flipping an image is essentially rotating it around an axes. Horizantal flipping is around Y-axis and Vertical flipping is around X-axis.
If you want to flip it both vertically and horizontally then you can do that too.

"""

__maintainer__ = "Nikunj Lad"

# importing relevant libraries
import cv2, argparse, sys

# parsing command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Input image to perform flipping operation")
args = vars(ap.parse_args())

# read the input image
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# Flip an image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Image flipped Horizontally", flipped)

# Flip an image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Image flipped vertically", flipped)

# Flip image both horizontally and vertically
flipped = cv2.flip(image, -1)
cv2.imshow("Image flipped both ways", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit()