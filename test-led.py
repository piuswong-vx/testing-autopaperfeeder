import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
# check pinout.xyz for pin diagram
print("LED on -- GPIO18, physical pin 12; grounded at physical pin 6")
GPIO.output(18,GPIO.HIGH)
time.sleep(10)

print("LED off")
GPIO.output(18,GPIO.LOW)
