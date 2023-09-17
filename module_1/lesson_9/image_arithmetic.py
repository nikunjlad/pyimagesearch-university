"""
_summary_

This script shows how to perform arithmetic operations like addition and subtraction on images. It also expands over the differences in Numpy and OpenCV based operations
"""

__maintainer__ = "Nikunj Lad"

# import relevant libraries
import cv2, argparse, sys
import numpy as np

# Performing arithmetic operations using OpenCV causes values to be clipped if they go beyond 0 or 255.
# To understand above statement, consider if a pixel value of 100 is added to 200. The result is 300. But pixels cannot be larger than 255 in value.
# So OpenCV will clip the result of an addition operation to 255 if values go beyond it.
# Likewis, for a subtraction operation, say 100 is subtracted from 50 resulting in -50. OpenCV will clip the result at 0 and not give -50 since 0 is the lower bound
# for a pixel value. It is better to use OpenCV for arithmetic to avoid confusion.
addition = cv2.add(np.uint8([200]), np.uint8([100]))
subtraction = cv2.subtract(np.uint8([50]), np.uint8([100]))
print(f"Adding 100 and 200 using OpenCV = {addition}")
print(f"Subtracting 100 from 50 using OpenCV = {subtraction}")

# Numpy arithmetic operations causes wrap around of values if they exceed lower and upper bounds of a pixel.
# Using above example, if addition of 200 and 100 causes 300, then instead of clipping, Numpy will restart counting from 0.
# So, 200 + 100 = 255 and then start counting from 0 again. This gives us value of 44 (since 255 in initial count and then restarting count from 0)
# Likewise, for subtraction, 50 - 100 will restarting count down from 255 since value is lower than 0
# So, 50 - 100 = -50 and then start counting down from 255 again. This gives us 206 as result
addition = np.uint8([200]) + np.uint8([100])
subtraction = np.uint8([50]) - np.uint8([100])
print(f"Adding 100 and 200 using Numpy (wrap around)= {addition}")
print(f"Subtracting 100 from 50 using Numpy (wrap around) = {subtraction}")

# parsing command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="../../data/images/sun.jpg", help="Input image to crop")
args = vars(ap.parse_args())

# read an image
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# adding 100 to all pixels of an image. this will yield a brighter image
M = np.ones(image.shape, dtype=np.uint8) * 100
bright = cv2.add(image, M)
cv2.imshow("Light image", bright)

# subtracting 50 from all pixels of an image. this will yield a dark image
M = np.ones(image.shape, dtype=np.uint8) * 50
dark = cv2.subtract(image, M)
cv2.imshow("Dark image", dark)

cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit(0)
