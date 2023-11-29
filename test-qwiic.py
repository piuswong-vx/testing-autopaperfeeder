# see https://github.com/sparkfun/Qwiic_Py

import qwiic

# For checking devices available:
results = qwiic.list_devices()
print(results)

import qwiic_i2c
test = qwiic_i2c.isDeviceConnected(0x60)
print(test)
