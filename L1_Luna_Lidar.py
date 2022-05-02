# 2022 MXET-300
# Author: Luke Baber
# TF-Luna Mini LiDAR wired to a BeagleBone Blue via UART

import Adafruit_BBIO.UART as UART
import numpy as np
import serial
import time    

UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=115200)
ser.close()

# Returns the distance in feet detected by the lidar
def tfluna_distance():
    while True:
        counter = ser.in_waiting
        if counter > 8:
            bytes_serial = ser.read(9) # read 9 bytes
            ser.reset_input_buffer() # reset buffer
    
            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256 # distance in next two bytes
                strength = bytes_serial[4] + bytes_serial[5]*256 # signal strength in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7]*256 # chip temp in next two bytes
                temperature = (temperature/8.0) - 256.0 # temp scaling and offset
                dist_feet = float(distance/100.0) * 3.28084
                return dist_feet
                

def serOpen():
    ser.open() 

def serClose():
    ser.close()

if __name__ == "__main__":
    ser.open()
    while True:
        time.sleep(0.1)
        distance = tfluna_distance() # read values
        print("Distance: %.3f" % distance, 'feet')
    ser.close()

# Prints out all the data from the TF Luna Lidar 
# distance,strength,temperature = read_tfluna_data() # read values
# print('Distance: {0:2.2f} m, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'.\
#               format(distance,strength,temperature)) # print sample data