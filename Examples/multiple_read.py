from machine import UART, Pin,SPI,I2C
import time,utime
from uhf import UHF
enable_pin = machine.Pin(4, machine.Pin.OUT)
enable_pin.value(0)

baudrate = 115200
uhf = UHF(baudrate)
uhf.multiple_read()
try:
    while 1:
        rev = uhf.read_mul()
        if rev is not None:
            #print(rev)
            print('EPC = ',"".join(rev[8:20]))
            print('RSSI(dBm) = ',rev[5])
            print('CRC = ',rev[20],rev[21])
        time.sleep(0.0009)
except KeyboardInterrupt:
    uhf.stop_read()
    time.sleep(1)
    print("stop")
   
