"""
_summary_

This script shows how to perform bitwise operations like AND, OR, XOR and NOT on sets of binary images. These operations are very useful later in CV while learning
Segmentation, Masking, Mask RCNN, etc
"""

__maintainer__ = "Nikunj Lad"

# import relevant libraries
import cv2, sys
import numpy as np

# Create images to play around
rectangle = np.zeros((300, 300), dtype=np.uint8)
rectangle = cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype=np.uint8)
circle = cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# Bitwise AND operation is when ONLY both the values of a pixel has a value of true it gives true else its false. Binary images have value of 255 (True) or 0 (False)
# 0 AND 0 is 0
# 0 AND 1 is 0
# 1 AND 0 is 0
# 1 AND 1 is 1
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwise_and)

# Bitwise OR operation is when either of the values of a pixel has a value of true it gives true else it gives false.
# 0 OR 0 is 0
# 0 OR 1 is 1
# 1 OR 0 is 1
# 1 OR 1 is 1
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwise_or)

# Bitwise XOR operation is same values give False and dis-similar values give True
# 0 XOR 0 is 0
# 0 XOR 1 is 1
# 1 XOR 0 is 1
# 1 XOR 1 is 0
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwise_xor)

# Bitwise NOT operation is just an inversion of the image. This is the only operation which takes a single image as input
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit(0)
