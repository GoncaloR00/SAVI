#!/usr/bin/env python3
import cv2
import numpy

#method = cv2.TM_SQDIFF

# Read the images from the file
scene = cv2.imread('images/scene.jpg')
wally = cv2.imread('images/wally.png')
#result = cv2.matchTemplate(scene, wally, method)
cv2.imshow('teste', wally)

""" # We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = wally.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(wally, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),5)

# Display the original image with the rectangle around the match.
cv2.imshow('output',scene) """

# The image is only displayed if we call this
cv2.waitKey(0)