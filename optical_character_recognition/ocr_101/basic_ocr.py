########################################################
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Nikunj Lad
#
# Basic script to perform OCR using PyTesserach library.
#
########################################################

__maintainer__ = "Nikunj Lad"

# importing relevant libraries
import argparse
import cv2
import sys
import pytesseract
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data/images"

# construct argument parser
ag = argparse.ArgumentParser()
# argument to load input images given its path
ag.add_argument("-i", "--input", default=DATA_DIR / "steve_jobs.png", help="path to input image")
args = vars(ag.parse_args())	# create a dictionary of the parsed command line arguments to be loaded for later use

# load image and convert it into RGB mode
image = cv2.imread(args["input"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Use PyTesseract to perform OCR on the image
text = pytesseract.image_to_string(image)
print(text)