#!/usr/bin/env python3

import cv2

scene = cv2.imread('images/scene.jpg')
wally = cv2.imread('images/wally.png')
h,w,_ = wally.shape
method = cv2.TM_CCOEFF
result = cv2.matchTemplate(scene, wally, method)
_,_,_,max_loc = cv2.minMaxLoc(result)
min_loc = (max_loc[0]+h, max_loc[1]+w)
cv2.rectangle(scene, max_loc, min_loc, (0,0,0),2)
cv2.imshow('resultado',scene)
cv2.waitKey(0)