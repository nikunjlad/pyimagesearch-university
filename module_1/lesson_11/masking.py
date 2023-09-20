"""
_summary_

This script shows how to perform masking on images to segment out ROI (regions of interest) using bitwise operations. Essentially a binary mask is used with the region
we want to extract as foreground and everything else acting as background.
"""

__maintainer__ = "Nikunj Lad"

# import relevant libraries
import cv2, sys, argparse
import numpy as np

# parsing command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="../../data/images/andy.jpg", help="Input image to crop")
args = vars(ap.parse_args())

# reading the image
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# body: BL = (x=307, y=599), TL = (x=307, y=7), TR=(x=894, y=7), BR = (x=894, y=599)
body_canvas = np.zeros(image.shape[:2], dtype=np.uint8)
body_mask = cv2.rectangle(body_canvas, (307, 7), (894, 599), 255, -1)
cv2.imshow("Body Mask", body_mask)

# extract body using body mask
# notice how for bitwise AND operation both source and the destination image are the same. That's because, we want to keep the original image channels of 3 but just tell
# OpenCV to leverage a binary mask to extract the region of interest.
body = cv2.bitwise_and(image, image, mask=body_mask)
cv2.imshow("Andy's Body", body)

# face: TL = (x=420, y=0), BL = (x=430, y=320), TR=(x=730, y=0), BR = (x=740, y=320)
face_canvas = np.zeros(image.shape[:2], dtype=np.uint8)
face_mask = cv2.circle(face_canvas, (580, 160), 160, 255, -1)
cv2.imshow("Face Mask", face_mask)

# extract face using face mask
face = cv2.bitwise_and(image, image, mask=face_mask)
cv2.imshow("Andy's Face", face)

cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit(0)
