# Use this code to help test if you've set up the relay connections properly.
# Hardware setup info here: https://github.com/votingworks/testing-autopaperfeeder

import RPi.GPIO as GPIO
import time
import sys

print("Running test-relay.py...")

# Set up output signal
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) #LED
GPIO.setup(23,GPIO.OUT) #STOP
GPIO.setup(24,GPIO.OUT) #START

try:
    print("set LED high")
    GPIO.output(18, GPIO.HIGH)
    start = time.time()
    time.sleep(1)

    print("set STOP (Relay 1) high")
    GPIO.output(23, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.02)

    print("set START (Relay 2) high")
    GPIO.output(24, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(24, GPIO.LOW)

    end = time.time()
    print("Time elapsed: ", end - start)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")

except:
    print("error!") 

finally:
    print("Ending GPIO control.") 
    GPIO.cleanup() # change all GPIO to input mode.