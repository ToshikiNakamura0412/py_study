import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def scale_to_resolation(img, resolation):
    """指定した解像度になるように、アスペクト比を固定して、リサイズする。
    """
    h, w = img.shape[:2]
    scale = (resolation / (w * h)) ** 0.5
    return cv.resize(img, dsize=None, fx=scale, fy=scale)


img = cv.imread('./photos/IMG_2319.JPG',0)
img = scale_to_resolation(img, 256 * 256)

# Initiate ORB detector
orb = cv.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()