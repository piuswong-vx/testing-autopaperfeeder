import qwiic_bme280
import qwiic_vl53l1x
import RPi.GPIO as GPIO
import time
import sys

# Set up output signal
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

print("Running sensor.py...")

def runSensors():

    print("\nVxWorks testing \n")
    
    # initialize sensors and data
    sensorAtmospheric = qwiic_bme280.QwiicBme280()
    sensorDist1 = qwiic_vl53l1x.QwiicVL53L1X()
    distance1 = 999
    distance1past = 999

    if sensorAtmospheric.is_connected() == False:
        print("The Qwiic BME280 (atmospheric) device isn't connected to the system.", 
            file=sys.stderr)
        return
    else:
        print("The Qwiic BME280 (atmospheric) device is online!")
        
    sensorDist1.sensor_init() 
    if (sensorDist1.sensor_init() == None):
        print("The Qwiic LV531X (IR distance) is online!")
    else:
        print("The Qwiic LV531X (IR distance) device isn't connected to the system.", 
            file=sys.stderr)
        return

    print("\n======\n")
    
    sensorAtmospheric.begin()

    while True:
        print("Humidity (RH):\t%.3f" % sensorAtmospheric.humidity)

        print("Pressure (kPa):\t%.3f" % sensorAtmospheric.pressure)    

        print("Altitude (ft):\t%.3f" % sensorAtmospheric.altitude_feet)

        print("Temp (F):\t%.2f" % sensorAtmospheric.temperature_fahrenheit)
        
        # distance code
        sensorDist1.start_ranging()
        distance1 = sensorDist1.get_distance()
        time.sleep(.005)
        sensorDist1.stop_ranging()
        print("Dist 1 (mm):\t%.1f" % distance1)
        if (distance1 < 200):
            print("** Distance sensor detects object! **")
            GPIO.output(18,GPIO.HIGH)
        else:
            GPIO.output(18,GPIO.LOW)
            if (distance1past < 200):
                print("* Object no longer detected. *")
        print("")                
        distance1past = distance1

        # wait
        time.sleep(1)

runSensors()
