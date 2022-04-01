# L3_drivingPatterns.py
# Team Number:
# Hardware TM:
# Software TM:
# Date:
# Code purpose: 
# indicate d1 and d2 distances:

# Import Internal Programs
import L2_speed_control as sc
import L2_inverse_kinematics as inv

# Import External programs
import numpy as np
import time
import L2_log as log
import L1_adc as adc

def task2():
	myVelocities = np.array([0.4, 0]) #input your first pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0.4,"forward_velocity.txt")
	log.uniqueFile(0,"angular_velocity.txt")
	time.sleep(2) # input your duration (s)
	
	myVelocities = np.array([0, ((np.pi)/2)]) #input your 2nd pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0,"forward_velocity.txt")
	log.uniqueFile((np.pi/2),"angular_velocity.txt")
	time.sleep(2.2) # input your duration (s)
	
	myVelocities = np.array([0.4, 0]) #input your 3rd pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0.4,"forward_velocity.txt")
	log.uniqueFile(0,"angular_velocity.txt")
	time.sleep(2) # input your duration (s)
	
	myVelocities = np.array([0, ((np.pi)/2)]) #input your 4th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0,"forward_velocity.txt")
	log.uniqueFile((np.pi/2),"angular_velocity.txt")
	time.sleep(2.2) # input your duration (s)
	
	myVelocities = np.array([0.4, 0]) #input your 5th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0.4,"forward_velocity.txt")
	log.uniqueFile(0,"angular_velocity.txt")
	time.sleep(2) # input your duration (s)
	
	myVelocities = np.array([0, -((np.pi)/2)]) #input your 6th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0,"forward_velocity.txt")
	log.uniqueFile(-(np.pi/2),"angular_velocity.txt")
	time.sleep(1) # input your duration (s)
	
	myVelocities = np.array([0.4, 0]) #input your 7th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0.4,"forward_velocity.txt")
	log.uniqueFile(0,"angular_velocity.txt")
	time.sleep(2) # input your duration (s)
	
	myVelocities = np.array([0, -((np.pi)/2)]) #input your 8th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0,"forward_velocity.txt")
	log.uniqueFile(-(np.pi/2),"angular_velocity.txt")
	time.sleep(1) # input your duration (s)
	
	myVelocities = np.array([0.4, 0]) #input your 9th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0.4,"forward_velocity.txt")
	log.uniqueFile(0,"angular_velocity.txt")
	time.sleep(2) # input your duration (s)
	
	myVelocities = np.array([0, 0]) #Stop the robot
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	log.uniqueFile(0,"forward_velocity.txt")
	log.uniqueFile(0,"angular_velocity.txt")
	time.sleep(2) # input your duration (s)
	
while (1):
    task2()
    dcJackVoltage = adc.getDcJack()                     
    log.uniqueFile(dcJackVoltage,"battery_voltage.txt")     
    time.sleep(0.2)