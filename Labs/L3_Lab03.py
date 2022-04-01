# L3_Lab03.py
# This program reads the DC voltage at barrel plug and magentometer to produce a cardinal heading

# Import Internal Programs
import L1_adc as adc
import L1_mpu as mpu
import L2_log as log
import L2_heading as heading

# Import External Libraries
import time
import numpy as np

# A function for saving a single line string to a log file in a temporary folder
def stringTmpFile(myString, fileName):     # this function takes a string and filename
    txt = open("/home/debian/basics/" + fileName, 'w+')   # file with specified name
    txt.write(myString)                    # by default the existing txt is overwritten
    txt.close()

def find_card_direction(heading_num):
     # North
    if headingDegrees < 22.5 or headingDegrees > 337.5:
        heading_num = "N"
     # North West
    elif headingDegrees > 22.5 and headingDegrees < 67.5:
        heading_num = "NW"
    # West
    elif headingDegrees > 67.5 and headingDegrees < 112.5:
        heading_num = "W"
    # South West
    elif headingDegrees > 112.5 and headingDegrees < 157.5:
        heading_num = "SW"
    # South
    elif headingDegrees > 157.5 and headingDegrees < 202.5:
        heading_num = "S"
    # South Est
    elif headingDegrees > 202.5 and headingDegrees < 247.5:
        heading_num = "SE"
    # East
    elif headingDegrees > 247.5 and headingDegrees < 292.5:
        heading_num = "E"
    # North East
    elif headingDegrees > 292.5 and headingDegrees < 337.5:
        heading_num = "NE"
    
    return heading_num

if __name__ == "__main__":
    while True:
        # Voltage from the battery
        dcJackVoltage = adc.getDcJack()   
        
        # Use this to reassign the cardinal direction
        card_direction = "N";
        axes = heading.getXY()                              # call xy function
        axesScaled = heading.scale(axes)                    # perform scale function
        h = heading.getHeading(axesScaled)                  # compute the heading
        headingDegrees = round(h*180/np.pi, 2)
        if headingDegrees < 0:
            headingDegrees = headingDegrees + 360
        
        print("heading:", headingDegrees)
        time.sleep(0.25)
        
        card_direction = find_card_direction(headingDegrees)
        
        print(card_direction)
        print("DC Jack Voltage: ", dcJackVoltage)
        
        # Add cardinal direction and direction to a .txt file for NodeRED
        log.uniqueFile(dcJackVoltage,"battery_voltage.txt")
        log.uniqueFile(headingDegrees,"heading.txt")
        stringTmpFile(card_direction,"cardinal_direction.txt")
        