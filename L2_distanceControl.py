# Basic distance control thread for MXET 300
# Reads information from luna lidar, checks if robot is too far away

import L1_Luna_Lidar as lidar
import L1_motors as motor
import L2_speed_control as sc
import L2_inverse_kinematics as inv

import time
import numpy as np

targetDist = 4.0

def controlCheck():
    
    
    if lidar.tfluna_distance() > targetDist:            # check distance from tracked object                                     # stop left motor
        print('stopped')                                # tell the user wtf is going on
        return True
    else:
        print('free move')                              # allow the robot to run away if its not too far from tracked face
        return False
        
if __name__ == "__main__":                              # main
    lidar.serOpen()
    while(1):
        controlCheck()
        time.sleep(0.2)
    lidar.serClose()
        
