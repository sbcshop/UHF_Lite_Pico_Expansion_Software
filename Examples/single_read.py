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

rev = uhf.single_read()
if rev is not None:
   print('EPC = ',rev[8:20])
   print('RSSI(dBm) = ',rev[5])
   print('CRC = ',rev[20],rev[21])

time.sleep(1)
uhf.stop_read()
   
