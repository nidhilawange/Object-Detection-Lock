import RPi.GPIO as GPIO
import time
import math
from remap import remap

#linking the correct GPIO pins to the ground, 
#5 V, and input connections on RasPi

GPIO.setmode(GPIO.BOARD)

#setup GPIO pin 11 as output and PWM so that servo moves in angled pattern back and forth
#clock cycle
GPIO.setup(13,GPIO.OUT)
servoMove = GPIO.PWM(13,50)
servoMove.start(0)

def setPos(angle: int):
    dc = remap(0,180,2,12,angle)
    servoMove.ChangeDutyCycle(dc)
    #print(dc)

def cleanup():
    GPIO.cleanup(11)

#Moving the servo motor shaft:
#2% (0 degrees) to 12% (180 degrees) duty cycle
#pulse width modulation controls high and low signal for degree movement

#
setPos(0)
if (__name__ == "__main__"): #if the image recognized passes, turn servo
    angle = 0
    #setPos(0)
    time.sleep(0.5)
    setPos(0)
    time.sleep(7)
    setPos(90)
    cleanup()







'''
time.sleep(3)
startCycle = 2
while (startCycle <= 12):
    servoMove.ChangeDutyCycle(startCycle)
    time.sleep(7)
    servoMove.ChangeDutyCycle(12)
    time.sleep(2)
    startCycle += 1
    time.sleep(2)
    exit()
'''




