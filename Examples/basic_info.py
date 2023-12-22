from machine import UART, Pin,SPI,I2C
import time,utime
from uhf import UHF
enable_pin = machine.Pin(4, machine.Pin.OUT)
enable_pin.value(0)

baudrate = 115200
uhf = UHF(baudrate)

'''
Uncomment corresponding section to increase reading range,
you will have to set the region as per requirment
'''
#uhf.setRegion_EU() 
#uhf.setRegion_US()

hw = uhf.hardware_version()
print('Hardware Version:',hw)
