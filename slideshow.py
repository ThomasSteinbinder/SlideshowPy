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

cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
x, y, sWidth, sHeight = cv2.getWindowImageRect('window')
#images = glob.glob("D:\\testImg\\2\\*.jpg")
images = glob.glob("C:\\Users\\Thomas\\Desktop\\photoframe\\*.jpg")

image1 = cv2.imread(images[0])
image1 = resizeImage(image1)
image1 = frameImage(image1)
cv2.imshow("window", image1)

i = 1;
count = len(images)
displayTime = 2000
fadeTime = 3000
fadeSteps = int(fadeTime / 100)
timePerFadeStep = int(fadeTime / fadeSteps)

while True:
    if i == count:
        i = 0
        
    image2 = cv2.imread(images[i])
    image2 = resizeImage(image2)
    image2 = frameImage(image2)
    
    cv2.waitKey(displayTime)
    
    for a in range(fadeSteps - 1, 0, -1):
        alpha = a / int(fadeTime / 100)
        blendImg = image1
        beta = ( 1.0 - alpha )
        cv2.addWeighted(image1, alpha, image2, beta, 0.0, blendImg)
        cv2.imshow("window", blendImg)
        cv2.waitKey(timePerFadeStep)
        
    image1 = image2
    cv2.imshow("window", image1)
    #cv2.waitKey(0)
    i += 1