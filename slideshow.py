# -----------------------------------------------------------
# Starts a slideshow using OpenCV
#
# (C) 2020 Thomas Steinbinder
# Released under GNU Public License (GPL)
# -----------------------------------------------------------

import ctypes
import glob
import cv2
import numpy as np

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sWidth = screensize[0]
sHeight = screensize[1]

def resizeImage(img):
    widthFactor = sWidth / img.shape[1]
    heightFactor = sHeight / img.shape[0]
    resizeFactor = widthFactor
    if heightFactor < widthFactor:
        resizeFactor = heightFactor
    newImg = cv2.resize(img, (0, 0), fx=resizeFactor, fy=resizeFactor)
    return newImg

def frameImage(img):
    newImg = np.zeros((sHeight, sWidth, 3), np.uint8)
    xOffset = int((newImg.shape[1] - img.shape[1]) / 2)
    yOffset = int((newImg.shape[0] - img.shape[0]) / 2)
    newImg[yOffset:img.shape[0] + yOffset,
           xOffset:img.shape[1] + xOffset] = img
    return newImg


images = glob.glob("D:\\testImg\\*.jpg")
#images = glob.glob("C:\\Users\\Thomas\\Desktop\\photoframe\\*.jpg")
cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

for i in range(0, len(images)):
    image = cv2.imread(images[i])
    image = resizeImage(image)
    image = frameImage(image)
    cv2.imshow("window", image)
    cv2.waitKey(0)