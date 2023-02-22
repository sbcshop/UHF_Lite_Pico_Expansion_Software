from machine import Pin, I2C, UART
from ssd1306 import SSD1306_I2C
from uhf import UHF
import time,utime

WIDTH  = 120                                            # oled display width
HEIGHT = 32                                             # oled display height

enable_pin = machine.Pin(4, machine.Pin.OUT) 
enable_pin.value(0) # Enable module

i2c = I2C(0,freq=200000,sda=Pin(20),scl=Pin(21))
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
    
oled.text("SB COMPONENTS",10,10)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()

baudrate = 115200
uhf = UHF(baudrate)
uhf.multiple_read()
try:
    while 1:
        rev = uhf.read_mul()
        if rev is not None:
            #print(rev)
            oled.text(str("".join(rev[8:20])),10,10)
            oled.show()
            print('EPC = ',"".join(rev[8:20]))
            print('RSSI(dBm) = ',rev[5])
            print('CRC = ',rev[20],rev[21])
        time.sleep(0.0009)
        oled.fill(0)
        oled.show()
except KeyboardInterrupt:
    uhf.stop_read()
    time.sleep(1)
    print("stop")


