"""
Code to load image from disk and to save image to disk
"""

__maintainer__ = "Nikunj Lad"

# importing relevant libraries
import argparse, cv2

# construct argument parser
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--input", required=True, help="path to input image")
ag.add_argument("-o", "--output", required=True, help="path to output image")
args = vars(ag.parse_args())

# load image from disk and grab spatial dimensions including width, height and channels
image = cv2.imread(args["input"])
(h, w, c) = image.shape[:3]

# display the image and print the image parameters
print(f"Width: {w} pixels")
print(f"Height: {h} pixels")
print(f"Channels: {c} channels")

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite(args["output"], image)
