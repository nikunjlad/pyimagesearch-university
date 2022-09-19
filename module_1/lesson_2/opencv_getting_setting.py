"""
Getting image pixel information, slicing images, updating pixel values and updating image regions
"""

__maintainer__ = "Nikunj Lad"

# import the necessary packages
import argparse, cv2

# construct argument parser
ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image", type=str, default="sunset.jpg", help="path to input image")
args = vars(ag.parse_args())

# load image and grab its spatial dimensions and display the image
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# fetch RGB values of top-left most pixel ie. corner pixels
(b, g, r) = image[0, 0]
print(f"Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}")

# access pixel information at x=50 and y=20
(b, g, r) = image[20, 50]
print(f"Pixel at (50,20) - Red: {r}, Green: {g}, Blue: {b}")

# update pixel information at x=50 and y=20
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print(f"Updated Pixel at (50,20) - Red: {r}, Green: {g}, Blue: {b}")

# compute center of the image
(cX, cY) = w // 2, h // 2

# slice the image into 4 quadrants based on above center information and display it
top_left_slice = image[0:cY, 0:cX]
top_right_slice = image[0:cY, cX:w]
bottom_left_slice = image[cY:h, 0:cX]
bottom_right_slice = image[cY:h, cX:w]
cv2.imshow("Top Left", top_left_slice)
cv2.imshow("Top Right", top_right_slice)
cv2.imshow("Bottom Left", bottom_left_slice)
cv2.imshow("Bottom Right", bottom_right_slice)

# setting top left area of the image to green and display it
image[0:cY, 0:cX] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
