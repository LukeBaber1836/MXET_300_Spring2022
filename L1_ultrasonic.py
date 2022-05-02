#This example takes a data point from the ultrasonic sensor (HC-SR04)
# and prints the data point, then repeats.

import Adafruit_BBIO.GPIO as GPIO
import time
import signal

echo_pin = 'P9_23'
trig_pin = 'GPIO1_25'
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(trig_pin, GPIO.OUT)
# i = 0

def distanceMeasurement(TRIG, ECHO):
    pulseEnd = 0
    pulseStart = time.time()
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while (GPIO.input(ECHO) == 0):# and (time.time()-pulseStart < 1):
        pulseStart = time.time()
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart
    #print pulseEnd- pulseStart
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance

def fall_detect():
    distance = distanceMeasurement(trig_pin, echo_pin)
    if distance > 9:
        print("Fall detected!")
        return True
        
    else:
        return False

if __name__ == "__main__":
    while True:
        fall_detect()
        distance = distanceMeasurement(trig_pin, echo_pin)
        print("Distance: ", distance, "cm")
        time.sleep(0.5)