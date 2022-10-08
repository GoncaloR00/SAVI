#!/usr/bin/env python3

import numpy as np
import cv2

def main():
    print('creating a image')
    image = np.ndarray((240,320,3), dtype=np.uint8)

    image += 129

    cv2.imshow('teste',image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()