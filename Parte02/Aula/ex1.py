#!/usr/bin/env python3

import cv2
import numpy as np

def main():
    image = cv2.imread('images/lake.jpg')
    h,w, _ = image.shape
    idx_middle = w/2
    image() -= 120
    cv2.imshow('teste', image)
    cv2.waitKey(0)



if __name__ == "__main__":
    main()