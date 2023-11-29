# Use this code to help test if the paper feeder is set up correctly.
# Hardware setup info here: https://github.com/votingworks/testing-autopaperfeeder

import RPi.GPIO as GPIO
import time
import sys

print("Running test-cuefeed.py...")

# Set up output signal
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) #LED
GPIO.setup(23,GPIO.OUT) #STOP
GPIO.setup(24,GPIO.OUT) #START

try:
    print("set LED high")
    GPIO.output(18, GPIO.HIGH)
    start = time.time()
    time.sleep(0.02)

    print("START for a few seconds.")
    print("START momentary signal...")
    timeSignal = 0.1
    timeRunning = 2.5
    GPIO.output(24, GPIO.HIGH)
    time.sleep(timeSignal)
    GPIO.output(24, GPIO.LOW)
    time.sleep(timeRunning)
    print("STOP momentary signal...")
    GPIO.output(23, GPIO.HIGH)
    time.sleep(timeSignal)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.02)

    end = time.time()
    print("Time elapsed: ", end - start)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")

except:
    print("error!") 

finally:
    print("Ending GPIO control.") 
    GPIO.cleanup() # change all GPIO to input mode.
