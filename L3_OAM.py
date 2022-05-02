# Names: Aaron Luna, Luke Baber, Kenneth Grau, Luis Luna
# Date: 5/3/2022
# Team Number: 
# Code Purpose: This program acts as our obstacle avoidance module

# Import Internal Programs
import L1_lidar as lid
import L1_Luna_Lidar as luna
import L2_vector as vec
import L2_speed_control as sc
import L2_inverse_kinematics as inv
import L2_distanceControl as distCont
import L1_ultrasonic as ultrs

import L1_adc as adc
import L2_log as log

# Import External programs
import numpy as np
import time


def obstacle():
    read = vec.getNearest() # grabs nearest obstacle m deg
    far = vec.getFarthest() # grabs farthest obstacle m deg
    
    # ultrs.fall_detect() == True
    # distCont.controlCheck() == True
    
    if (distCont.controlCheck() == False):
        #log.stringTmpFile("Fall Detected", "ult.txt")
        log.stringTmpFile("Person is not in proper distance", "luna.txt")
        myVelocities = np.array([0, 0]) #input your first pair
        myPhiDots = inv.convert(myVelocities)
        sc.driveOpenLoop(myPhiDots)
        log.stringTmpFile("SCUTTLE stopped", "scuttle_motion.txt")
        scuttle_angle = 'stopped'
    
    elif (read[0] < 0.40) and (-20 < read[1] < 20): # middle
        slowdown()
        middle()
        log.stringTmpFile("No Fall Detected", "ult.txt")
        print("object directly infront")
        if far[1] > 0:
            right()
            scuttle_angle = "left"
            log.stringTmpFile("SCUTTLE is turning left", "scuttle_motion.txt")
            print("adjusting to go left")
        elif far[1] < 0:
            left()
            scuttle_angle = "right"
            log.stringTmpFile("SCUTTLE is turning right", "scuttle_motion.txt")
            print("adjusting to go right")
            
    elif (read[0] < 0.30) and (-135 <= read[1] <= -20): # detects right moves left
        slowdown()
        right()
        scuttle_angle = "left"
        log.stringTmpFile("SCUTTLE is turning left", "scuttle_motion.txt")
        print("moving right")
        log.stringTmpFile("No Fall Detected", "ult.txt")

    elif (read[0] < 0.30) and (20 <= read[1] <= 135): # detects left moves right
        slowdown()
        left()
        scuttle_angle = "right"
        log.stringTmpFile("SCUTTLE is turning right", "scuttle_motion.txt")
        print("moving left")
        log.stringTmpFile("No Fall Detected", "ult.txt")

    else: # keeps moving forward
        myVelocities = np.array([0.4, 0])
        myPhiDots = inv.convert(myVelocities)
        sc.driveOpenLoop(myPhiDots)
        time.sleep(0.01) # input your duration (s)
        scuttle_angle = "forward"
        log.stringTmpFile("SCUTTLE is driving forward", "scuttle_motion.txt")
        print("running")
        log.stringTmpFile("No Fall Detected", "ult.txt")

    
    log.stringTmpFile("Person is in proper distance", "luna.txt")
    log.tmpFile(far[1], "far_distance.txt")
    log.tmpFile(read[0], "clo_distance.txt")
    log.tmpFile(read[1], "clo_angle.txt")
    print("Closet Distance (m) and Angle Alpha (deg): ", read)
    print("Farthest Distance (m) and Angle Alpha (deg): ", far)
    
    return scuttle_angle
        
def slowdown(): #slows down the motor
    myVelocities = np.array([0.2, 0])
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(0.2) # input your duration (s)    
    
def middle(): #detects something directly infront
    myVelocities = np.array([0, 0])
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    log.stringTmpFile("SCUTTLE stopped", "scuttle_motion.txt")
    time.sleep(0.5) # input your duration (s)
    
    myVelocities = np.array([-0.25, 0])
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    log.stringTmpFile("SCUTTLE is reversing", "scuttle_motion.txt")
    time.sleep(2) # input your duration (s)

def right(): #detects right moves left
    myVelocities = np.array([0, 1.225])
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1) # input your duration (s)

    
def left(): #detects left moves right
    myVelocities = np.array([0, -1.225])
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1) # input your duration (s)


def go():
    luna.serOpen()
    
    while(1):
        scuttle_angle = obstacle()
        print("Scuttle Heading Angle: ", scuttle_angle)

        # dcJackVoltage = adc.getDcJack()                     # call the getDcJack function from within L1_adc.py
        # print("DC Jack Voltage: ", dcJackVoltage)           # print the dc jack voltage to the terminal 
        # print(" ")
        # log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")        # log the dc jack voltage to the tmp file directory
        
        # # time.sleep(0.2)
        # time.sleep(1)
        # print(2)


if __name__ == "__main__":
    
    luna.serClose()
    luna.serOpen()
    
    print("Enter something:  ")
    x = input()
    
    while(1):
        scuttle_angle = obstacle()
        print("Scuttle Heading Angle: ", scuttle_angle)
        
        dcJackVoltage = adc.getDcJack()                     # call the getDcJack function from within L1_adc.py
        print("DC Jack Voltage: ", dcJackVoltage)           # print the dc jack voltage to the terminal 
        print(" ")
        log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")        # log the dc jack voltage to the tmp file directory
        
        time.sleep(0.5)
