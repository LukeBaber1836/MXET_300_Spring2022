# Names: Aaron Luna, Luke Baber, Kenneth Grau, Luis Luna
# Date: 5/3/2022
# Team Number: 
# Code Purpose: This program detects if there is a fall with the ultrasonic sensor for the SCUTTLE

# Import external libraries
import L1_ultrasonic as ult
import L1_lidar as lid
import L2_vector as vec
import L2_speed_control as sc
import L2_inverse_kinematics as inv

import L1_adc as adc
import L2_log as log

# Import internal programs
import numpy as np
import time

def falldetection():
    fall = ult.distanceMeasurement('GPIO1_25', 'P9_23') # prints height ultrasonic sensor is detecting
    #print("Height detected: ", fall)  
    if fall > 9:
        print("There is a drop ahead, SCUTTLE has stopped")
        return True
        
    else:
        print("No Fall")
        return False


if __name__ == "__main__":
    while(1):
        falldetection()
        time.sleep(0.2)