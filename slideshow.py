# -----------------------------------------------------------
# Starts a slideshow using OpenCV
#
# (C) 2020 Thomas Steinbinder
# Released under GNU Public License (GPL)
# -----------------------------------------------------------

import glob
from os.path import join
import cv2
import numpy as np

# Resizes an image to fit in the screen resolution
def resize_image(img):
    width_factor = screen_width / img.shape[1]
    height_factor = screen_height / img.shape[0]
    resize_factor = width_factor
    if height_factor < width_factor:
        resize_factor = height_factor
    new_img = cv2.resize(img,
                         (0, 0),
                         fx=resize_factor,
                         fy=resize_factor)                         
    return new_img

# Generates an image of the size of the screen
# and places a given image centered inside it.
def frame_image(img):
    new_img = np.zeros((screen_height, screen_width, 3), np.uint8)
    x_offset = int((new_img.shape[1] - img.shape[1]) / 2)
    y_offset = int((new_img.shape[0] - img.shape[0]) / 2)
    new_img[y_offset:img.shape[0] + y_offset,
           x_offset:img.shape[1] + x_offset] = img           
    return new_img


#image_path = "C:\\Users\\Thomas\\Desktop\\photoframe\\"
image_dir = "D:\\testImg\\2\\"
images = []
for ext in ('*.jpg', '*.jpeg', '*.bmp', '*.png'):
    images.extend(glob.glob(join(image_dir, ext)))   
count = len(images)

if count == 0:
    exit();

cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('window',
                       cv2.WND_PROP_FULLSCREEN,
                       cv2.WINDOW_FULLSCREEN)
x, y, screen_width, screen_height = cv2.getWindowImageRect('window')
i = 1;
display_time = 2000
fade_time = 3000
fade_steps = int(fade_time / 100)
time_per_fade_step = int(fade_time / fade_steps)

image1 = cv2.imread(images[0])
image1 = resize_image(image1)
image1 = frame_image(image1)
cv2.imshow("window", image1)

while True:
    if i == count:
        i = 0        
    image2 = cv2.imread(images[i])
    image2 = resize_image(image2)
    image2 = frame_image(image2)
    blend_img = image1
    
    cv2.waitKey(display_time)
    
    # Blending images
    for a in range(fade_steps - 1, 0, -1):
        alpha = a / fade_steps
        beta = ( 1.0 - alpha )     
        cv2.addWeighted(image1, alpha,
                        image2, beta,
                        0.0, blend_img)
        cv2.imshow("window", blend_img)
        cv2.waitKey(time_per_fade_step)
        
    image1 = image2
    cv2.imshow("window", image1)
    i += 1