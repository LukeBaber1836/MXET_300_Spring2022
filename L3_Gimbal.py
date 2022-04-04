import time, math
import getopt, sys
import rcpy  # This automatically initizalizes the robotics cape
import rcpy.servo as servo
import rcpy.clock as clock	# For PWM period for servos

# Import Internal Programs
import L1_servo as srv

def move_servos():
    # Move 1 Degree at a time servo 1
    srv.move1(1.5)
    time.sleep(0.2)
    # Move 1 Degree at a time servo 2
    srv.move2(1.5)
    time.sleep(0.2)
    
    # Return to normal position
    srv.move1(-1.5)
    time.sleep(0.2)
    srv.move2(-1.5)
    time.sleep(0.2)
    
    
    
while (1):
    move_servos()