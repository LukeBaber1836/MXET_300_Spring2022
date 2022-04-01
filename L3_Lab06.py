# Lab 06 Code


import L1_adc as adc
import L1_lidar as lid
import L2_vector as vect
import L2_log as log

while 1:
    
    near = vect.getNearest()
    print(near)

    log.tmpFile(near[0],"Distance")
    log.tmpFile(near[1],"Angle")
    
    cart = vect.polar2cart(near[0],near[1])
    log.tmpFile(cart[0],"dX")
    log.tmpFile(cart[1],"dY")
    print(cart)
    
    log.tmpFile(adc.getDcJack(),"Voltage")
    






