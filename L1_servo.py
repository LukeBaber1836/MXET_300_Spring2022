# Import external libraries
import time, math
import getopt, sys
import rcpy  # This automatically initizalizes the robotics cape
import rcpy.servo as servo
import rcpy.clock as clock	# For PWM period for servos

# INITIALIZE DEFAULT VARS
duty = 1.5		# Duty cycle (-1.5,1.5 is the typical range)
period = 0.02 	# recommended servo period: 20ms (this is the interval of commands)
ch1 = 1			# select channel (1 thru 8 are available)
ch2 = 2			# selection of 0 performs output on all channels

rcpy.set_state(rcpy.RUNNING) # set state to rcpy.RUNNING
srvo1 = servo.Servo(ch1)	# Create servo object
srvo2 = servo.Servo(ch2)
clck1 = clock.Clock(srvo1, period)	# Set PWM period for servos
clck2 = clock.Clock(srvo2, period)

servo.enable()		# Enables 6v rail on beaglebone blue
clck1.start()		# Starts PWM
clck2.start()

def set_angle( angle ):		#input angle 0 - 180
	pwm_val = 0
	# For pwm -1.5 to 0
	if angle <= 90:
		# Scale degrees to pwm value
		pwm_val = float(1.5/90) * angle - 1.5
		srvo1.set(pwm_val)
	# For pwm 0 to 1.5
	else:
		# Scale degrees to pwm value
		angle = angle - 90
		pwm_val = float(1.5/90) * angle
		srvo1.set(pwm_val)
		
def set_origin():
	# Make sure camera starts at orgin, 90 deg or PWM 0.
	set_angle(90);

# Protects servo from going out of range
def check_angle( angle ):
	if angle > 180 or angle < 0:
		angle = 90
	return angle
	
def move2(angle):
	srvo1.set(angle)
	

# THE SECTION BELOW WILL ONLY RUN IF L1_SERVO.PY IS CALLED DIRECTLY	 
# if __name__ == "__main__":
#     # keep running
# 	while rcpy.get_state() != rcpy.EXITING:
# 		angle = 0
# 		angle = input("Enter angle 0 - 180 degrees:  ")
# 		angle_f = float(angle)
# 		move1(angle_f)
