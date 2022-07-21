import servo
import time

def unlock():
    servo.setPos(90)

def lock():
    servo.setPos(0)

def  cleanup():
    servo.cleanup()

if (__name__ == "__main__"):
    unlock()
    time.sleep(1)
    lock()
    time.sleep(1)


