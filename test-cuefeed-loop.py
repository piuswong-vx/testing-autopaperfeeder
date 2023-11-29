# Use this code to help test if the paper feeder is set up correctly.
# This is meant to send out a stack of sheets of paper, one by one.
# Hardware setup info here: https://github.com/piuswong-vx/sandbox-rpi

import RPi.GPIO as GPIO
import time
import sys

print("Running test-cuefeed-loop.py...")

# Set up output signal
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) #LED

# define these parameters according to desired system setup
time.sleep(0.02)
timeSignal = 0.1    # length of momentary signal trigger
timeRunning = 2.5   # default length of time after start signal to stop 
pinStop = 23
pinStart = 24

class Feeder:
    def __init__(self, pinStop, pinStart, timeSignal):
        self.timeSignal = timeSignal
        self.timeRunning = timeRunning
        self.pinStop = pinStop
        self.pinStart = pinStart
        GPIO.setup(pinStop,GPIO.OUT) #STOP
        GPIO.setup(pinStart,GPIO.OUT) #START

    def start(self,timeRunning):
        print("START momentary signal...")
        GPIO.output(self.pinStart, GPIO.HIGH)
        time.sleep(timeSignal)
        GPIO.output(self.pinStart, GPIO.LOW)
        time.sleep(timeRunning)

    def stop(self):
        print("STOP momentary signal...")
        GPIO.output(self.pinStop, GPIO.HIGH)
        time.sleep(timeSignal)
        GPIO.output(self.pinStop, GPIO.LOW)

feeder = Feeder(pinStop, pinStart, timeSignal)

try:
    print("set LED high")
    GPIO.output(18, GPIO.HIGH)
    start = time.time()
    
    while True:
        print("** START for a few seconds. **")
        feeder.start(timeRunning)
        feeder.stop()
        time.sleep(1)
        end = time.time()
        print("Time elapsed: ", end - start)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")
    print("STOP momentary signal...")
    feeder.stop()

except:
    print("error!") 
    feeder.stop()

finally:
    print("Ending GPIO control.") 
    GPIO.cleanup() # change all GPIO to input mode.
