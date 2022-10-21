"""
Doing basic drawing on canvases - lines, rectangles, circles
"""

__maintainer__ = "Nikunj Lad"

# import relevant libraries
import cv2
import numpy as np
import sys

# initialize a blank numpy canvas to draw our objects using opencv
canvas = np.zeros((500, 500, 3), dtype="uint8")

# draw a green line from top-left to bottom-right corner of the image
green = (0, 255, 0)  # green color since BGR
cv2.line(canvas, (0, 0), (300, 300), green)  # we draw a line on the canvas, given start point and end point and also color in which to draw
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a red line of thickness 3 from top-right to bottom-left of the image
red = (0, 0, 255)  # red color since BGR
cv2.line(canvas, (500, 0), (0, 500), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a 50x50 rectange, starting at 10,10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (100, 100), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a 250x100 rectangle of 5px thickness
cv2.rectangle(canvas, (50, 300), (300, 400), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a rectangle which is filled in with color instead of just a border and hollow interior
blue = (255, 0, 0)
cv2.rectangle(canvas, (400, 50), (450, 350), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# reinitialize canvas to draw circles now
canvas = np.zeros((400, 400, 3), dtype="uint8")  # creating a 400x400 black canvas
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)  # get the center of the canvas value
white = (255, 255, 255)  # color white

# loop over increasing radius and draw concentric circles to create a bulls eye pattern
for r in range(0, 225, 25):
	cv2.circle(canvas, (centerX, centerY), r, white, 2)  # create circles over the canvas with incremental radius values in steps of 25

# display the bullseye pattern
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# reinitialize canvas to draw 25 random circles
canvas = np.zeros((1000, 1000, 3), dtype="uint8")

# loop to draw 25 random circles of random centers, colors and radiuses
for i in range(0, 25):
	radius = np.random.randint(low=20, high=400)  # randomly generate radius in range of 20-800 px values
	color = np.random.randint(low=0, high=256, size=(3,)).tolist()  # randomly generate color values of the color spectrum
	center = np.random.randint(low=0, high=1000, size=(2,))  # randomly generate center point to draw circle around

	# draw the circle on the canvas
	cv2.circle(canvas, center, radius, color, -1)

# display the pattern
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit(0)
