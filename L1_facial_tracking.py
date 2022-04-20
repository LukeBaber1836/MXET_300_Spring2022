# OpenCV program to detect face in real time
import cv2
import array as arr
import numpy as np
import time, math
import L1_servo as servo

# Face tracker XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

size_w = 240    # Resized image width. This is the image width in pixels
size_h = 160    # Resized image height. This is the image height in pixels

# capture frames from a camera
cap = cv2.VideoCapture(0)
cap.set(3, size_w)                       # Set width of images that will be retrived from camera
cap.set(4, size_h)                       # Set height of images that will be retrived from camera

def get_origin_x():
    # reads frames from a camera
    ret, img = cap.read()
    origin_x = 0
    width = 0

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # find origin
        width = w
        origin_x = x + (w/2)
        #origin_y = y + (h/2)
    return origin_x, width
    
    
# Moves servo to center camera on object, returns current angle of the camera
def center_face( current_angle ):
    x_val = get_origin_x()
    print(x_val)
    
    # continue if no object found 
    if x_val == 0:
        return current_angle
    
    # Move gimbal to recenter the object
    if x_val < 135:
        current_angle = current_angle + 4
        current_angle = servo.check_angle( current_angle )
        servo.set_angle( current_angle)
        return current_angle
    
    elif x_val > 200:
        current_angle = current_angle - 4
        current_angle = servo.check_angle( current_angle )
        servo.set_angle( current_angle )
        return current_angle


if __name__ == "__main__":
    #servo.set_origin()
    curr_angle = 90
    
    while(1):
        x, w = get_origin_x()
        print(x)        