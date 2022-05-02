# color_tracking_v1.py
# usb camera: Microsoft HD-3000 target: orange basketball
# This program was designed to have SCUTTLE following a basketball.
# The calibration was made in a brightly lit indoor environment.
# Video demo: https://youtu.be/9t1XHcomlIs
# color Tracking
import cv2              # For image capture and processing
import argparse         # For fetching user arguments
import numpy as np      # Kernel
import time

import rcpy                 # Import rcpy library
import rcpy.motor as motor  # Import rcpy motor module

filter = 'HSV'  # Use HSV to describe pixel color values

def face_x( camera ):
    x = 0  # will describe target location left to right
    y = 0  # will describe target location bottom to top

    radius = 0  # estimates the radius of the detected target
    
    scale_t = 1.3	# a scaling factor for speeds
    scale_d = 1.3	# a scaling factor for speeds

    ret, image = camera.read()  # Get image from camera

    height, width, channels = image.shape   # Get size of image

    if filter == 'RGB':                     # If image mode is RGB switch to RGB mode
        frame_to_thresh = image.copy()
    else:
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    # Otherwise continue reading in HSV

    thresh = cv2.inRange(frame_to_thresh, (165, 0, 0), (255, 255, 255))   # Find all pixels in color range

    kernel = np.ones((5,5),np.uint8)                            # Set gaussian blur strength.
    mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)     # Apply gaussian blur
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]     # Find closed shapes in image
    center = None   # Create variable to store point

    if len(cnts) > 0:   # If more than 0 closed shapes exist

        c = max(cnts, key=cv2.contourArea)              # Get the properties of the largest circle
        ((x, y), radius) = cv2.minEnclosingCircle(c)    # Get properties of circle around shape
        x = int(x)
        # print(x)
        return (x)

# exiting program will automatically clean up cape

if __name__ == '__main__':
    
    camera = cv2.VideoCapture(0)     # Define camera variable
    camera.set(3, 240)                       # Set width of images that will be retrived from camera
    camera.set(4, 160)                       # Set height of images that will be retrived from camera
    
    while(1):
        print (face_x( camera ))