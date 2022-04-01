# Lab 05 Code
# This code takes and prints the xDot and thetaDot values from the L1_econder.py and L2_kinematics.py

import L2_kinematics as kin
import L1_encoder as enc
import L2_log as log
import L1_adc as adc
import numpy as num
import time
from time import sleep

while 1:
    phis = kin.getPdCurrent()
    print(phis)
    motion = kin.getMotion()
    print(motion)
    dc = adc.getDcJack()
    
    log.tmpFile(phis[0],"leftPhi")
    log.tmpFile(phis[1],"rightPhi")
    log.tmpFile(motion[0],"xDot")
    log.tmpFile(motion[0],"thetaDot")
    log.tmpFile(dc,"dcVoltage")
    
    






