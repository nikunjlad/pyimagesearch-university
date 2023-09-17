"""
_summary_

This script shows how to resize an image using various interpolation methods. It also shows how to maintain the aspect ratio of the image while resizing an image up or down.
Finally, we also recommended the best resize operations and techniques to use for our resize operations based on the conditions and situations we encounter.

"""

__maintainer__ = "Nikunj Lad"

# importing relevant libraries
import cv2, argparse, imutils, sys

# create argument parser handler
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ag.parse_args())

# read the image
image = cv2.imread(args["image"])
(height, width) = image.shape[0:2]  # get the height and width of the image
aspect_ratio = width * 1.0 / height
cv2.imshow("Original Image", image)

# Resize the image maintaining the aspect ratio to have width of 150 pixels
new_height = int(150 / aspect_ratio)
resized_image = cv2.resize(image, (150, new_height), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized image with width 150", resized_image)

# Resize the image maintaining the aspect ratio to have height of 50 pixels
new_width = int(50 * aspect_ratio)
resized_image = cv2.resize(image, (new_width, 50), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized image with height 50", resized_image)

# Resize images using imutils to avoid performing math operations for aspect ratio resizing
# When you resize images using imutils, you can provide the desired width and height to resize the image to. The aspect ratio is automatically handled by the library
# Resize the image using imutils to a width of 100
resized_image = imutils.resize(image, width=100)
cv2.imshow("Resized image using imutils", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize images using various interpolation methods.
# Use first three methods to resize down an image from a higher resolution since its fast operation. Preferably, use cv2.INTER_LINEAR to make an image smaller with best results
# Use last 2 methods to resize up an image from a lower resolution since its more accurate. Preferably, use cv2.INTER_CUBIC to make an image larger with best results.
resize_methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LACZOS4", cv2.INTER_LANCZOS4),
]

cv2.imshow("Original Image", image)
for (name, method) in resize_methods:
    print(f"Resizing image using {name}")
    resized_image = imutils.resize(image, width=width * 3, inter=method)
    cv2.imshow(f"Image resized using {name}", resized_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
sys.exit(0)