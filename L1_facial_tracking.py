# OpenCV program to detect face in real time
import cv2
import time, math
import L1_servo as servo
import rcpy                 # Import rcpy library
import color_tracking_v1 as color_t
import L2_log as log


def center_face( x_val, current_angle ):
    # x_val = color_t.face_x()
    
    # Make sure object is detected
    if x_val is not None:
        #print(x_val)
        # Move gimbal to recenter the object
        # To far left
        if x_val < 90:
            current_angle = current_angle + 2
            current_angle = servo.check_angle( current_angle )
            servo.set_angle( current_angle)
            return current_angle
        
        # To far right
        elif x_val > 150:
            current_angle = current_angle - 2
            current_angle = servo.check_angle( current_angle )
            servo.set_angle( current_angle )
            return current_angle
        
        # Object is centered
        else:
            return current_angle
    
    else:
        return current_angle

def move_angle( x_val ):
    # Each angle is approximately 4.375 degrees
    if x_val > 120:                     # Move left
        angle = (x_val / 3) - 40
        return int(angle)
        
    elif x_val <= 120 and x_val != 0:   # Move right
        angle = -((x_val / 3) - 40)
        return int(angle)
    
    # Sets gimbal to origin value
    else:
        return 0
        
def go():
    servo.set_origin()
    curr_angle = 90
    
    camera = cv2.VideoCapture(0)     # Define camera variable
    camera.set(3, 240)                       # Set width of images that will be retrived from camera
    camera.set(4, 160)  
    
    while(1):
        # time.sleep(0.01)
        x_val = color_t.face_x( camera )
        curr_angle = center_face( x_val,  curr_angle )
        print( curr_angle )
        #face_distance( width )
        #print(width)


if __name__ == "__main__":
    servo.set_origin()
    curr_angle = 90
    
    camera = cv2.VideoCapture(0)     # Define camera variable
    camera.set(3, 240)                       # Set width of images that will be retrived from camera
    camera.set(4, 160)  
    
    while(1):
        x_val = color_t.face_x( camera )
        curr_angle = center_face( x_val,  curr_angle )
        log.tmpFile(curr_angle, "servo.txt")
        print( curr_angle )
        #face_distance( width )
        #print(width)
               