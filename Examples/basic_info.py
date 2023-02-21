from machine import UART, Pin,SPI,I2C
import time,utime
from uhf import UHF
enable_pin = machine.Pin(4, machine.Pin.OUT)
enable_pin.value(0)

baudrate = 115200
uhf = UHF(baudrate)
hw = uhf.hardware_version()
print('Hardware Version:',hw)
