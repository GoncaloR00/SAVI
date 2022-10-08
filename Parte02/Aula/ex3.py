#!/usr/bin/env python3

import cv2
import numpy as np

scene = cv2.imread('images/scene.jpg')
wally = cv2.imread('images/wally.png')
h,w,_ = wally.shape
method =cv2.TM_CCOEFF
result = cv2.matchTemplate(scene, wally, method)
_,_,_,max_loc = cv2.minMaxLoc(result)
min_loc = (max_loc[0]+h, max_loc[1]+w)
se_gray = cv2.COLOR_BGR2GRAY(scene)
image_gui = scene * 0
wally_loc = 
cv2.imshow('resultado',wally.loc)
cv2.waitKey(0)