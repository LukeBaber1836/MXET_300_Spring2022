import time, math
import L1_facial_tracking as facial
import L1_servo as servo

# Returns 0: on target, 1: left, 2: right
def determine_dir():
    # Change these values to adjust the tolerance of the camera tracking
    left_min = 145.0
    right_max = 175.0
    origin_x = 0
    origin_x = facial.get_origin_x()
    dir_val = 0
    
    if left_min < origin_x < right_max:
        # On target
        dir_val = 0
    elif origin_x < left_min:
        # Left
        dir_val = 1
    else:
        # Right
        dir_val = 2
    
    return dir_val

def center_camera( current_angle ):
    orientation = determine_dir()
    if dir_val == 1:
        # Left
        servo.set_angle(current_angle + 1)
        center_camera(current_angle)
        
    elif  dir_val == 2:
        # Right
        servo.set_angle(current_angle - 1)
        center_camera(current_angle)
    else:
        # Base case
        print ("Centered")


# Run to demonstrate gimbal tracking
if __name__ == "__main__":
    servo.set_origin()
    curr_angle = servo.set_origin()
    # Run continually to track face
    while 1:
        center_camera(curr_angle)
        