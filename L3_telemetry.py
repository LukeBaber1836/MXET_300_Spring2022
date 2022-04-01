# L3_telemetry.py
# This program grabs data from the onboard sensors and log data in files
# for NodeRed access and integrate into a custom "flow".
# Access nodered at 192.168.8.1:1880 (by default, it's running on the Blue)

# Import Internal Programs
import L1_mpu as mpu
import L1_adc as adc
import L1_bmp as bmp
import L2_log as log

# Import External programs
import numpy as np
import time

# Run the main loop
while True:
    accel = mpu.getAccel()                          # call the function from within L1_mpu.py
    (xAccel) = accel[0]                             # x axis is stored in the first element
    (yAccel) = accel[1]                             # y axis is stored in the second element
    (zAccel) = accel[2]
    print("x axis:", xAccel, "y axis:", yAccel, "z axis:", zAccel)      # print the three values
    axes = np.array([xAccel, yAccel, zAccel])                           # store axes in an array
    log.uniqueFile(axes[0],"xAccel.txt")                                # send vlues to txt files for nodered
    log.uniqueFile(axes[1],"yAccel.txt")
    log.uniqueFile(axes[2],"zAccel.txt")
    
    bat = adc.getDcJack()                           # call the function from within L1_adc.py
    print("bat:", bat)                              # print value
    log.uniqueFile(bat,"bat.txt")                   # send the data to txt files for NodeRed to access.
    
    temp = bmp.temp()
    pres = bmp.pressure()
    alt = bmp.altitude()
    print("temp:", temp, "pressure:", pres, "altitude:", alt)   #print value
    log.uniqueFile(temp,"temp.txt")                             #log temperature data to txt file
    log.uniqueFile(pres,"pressure.txt")                         #log pressure data to txt file
    log.uniqueFile(alt,"altitude.txt")                          #log altitude data to txt file
    
                                                    # send the data to txt files for NodeRed to access.
    # log.uniqueFile(xAccel,"xAccel.txt")           # another way to log data for NodeRed access
    # log.uniqueFile(yAccel,"yAccel.txt")
    # log.tmpFile(xAccel,"xAccel.txt")              # another way to lof data for NodeRed access
    # log.tmpFile(yAccel,"yAccel.txt")
    
    time.sleep(0.2)
