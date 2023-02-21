# UHF_Lite_Pico_Expansion_Software

The frequency range of the UHF (Ultra High Frequency) Lite Expansion, a radio frequency device, is 300 MHz to 3 GHz. Wireless communication systems, such as radio-frequency identification (RFID) systems, Wi-Fi networks, and other short-range wireless communication applications, frequently employ UHF modules. UHF modules are created to send and receive signals over brief distances, usually up to a few hundred metres, and they have benefits like fast data transmission rates, low power consumption, and inexpensive price. Moreover, Anteena is on board.

<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img10.png"/>

## Features/Specifications(Module):
  * Operating Voltage of DC 3.5-5volt
  * Operating Temprature -20 C to -70 C
  * Frequency 840 to 960MHz
  * Support RSSI Tags
  * TTL UART interface
  * Default and recommend communication baud rate is 115200 bps
  * Output power is 18-26 dbm
  * Protocol - EPCglobal UHF Class 1 Gen 2 / ISO 18000-6C
  * Frequency - 840-960MHZ
  * Output power- 18 to 26 dBm
  * Tags RSSI support
  * Air cooling(no need for out install cooling fan）
## Onboard antenna character：
  * Be sensitive and stable to the tags identify.
  * Stable reading distance 1 meter and Reading distance speed, >50pcs/sec.
  * Muti-tags identify, >50pcs tags.

## Hardware Overview
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img11.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img13.png"/>

## Steps To Setup The UHF Lite UHF Expansion
Make sure connect jumper wire as per below image, while UHF Expansion use ***with*** PICO

<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img12.png"/>
1. Download Thonny IDE 

   https://thonny.org/
   
   <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img.JPG" />
   
2. Install MicroPython in Raspberry pi PICO
     first you need to press the boot button then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new device named         "RPI-RP2" drag this file "firmware.uf2" to this device as shown in figure
        <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />
   ### Learning Guide
      * [Getting Started with Micropython](https://github.com/sbcshop/SquaryPi-Software/tree/main/Python_Package) - Step by step guide to start with Micropython

## Code
Download the repository, This repository have two folder :

 * Library - Inside this folder there is a file name  ***uhf.py*** and ***ssd1306.py*** (UHF Module Library)

   [Library](https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Library/uhf.py), Save these file inside Raspberry Pi PICO
 
 * Examples - Inside this folder there are many examples :
 
   [Examples](https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/tree/main/Examples)

## Configure UHF Lite from Application
You can download this application from below link:

[UHF Software](https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/uhf%20lite.rar)

<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img.JPG"/>

Connect USB to UHF HAT
Make sure connect jumper wire as per below image, while UHF Expansion use ***without*** PICO

<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/UHF%20Lite.jpg"/>
Make sure change the jumper wire as per upper image

<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img1.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img2.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img3.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img4.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img5.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img6.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img7.png"/>
<img src = "https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/Images/img8.png"/>

## UHF Lite Expansion Command Manual
[Command Manual](https://github.com/sbcshop/UHF_Lite_Pico_Expansion_Software/blob/main/UHF%20Lite%20Manual.docx)


## Related Products

* [UHF Lite HAT](https://shop.sb-components.co.uk/products/uhf-rfid-lite-hat) - Raspberry Pi Version

 ![UHF Lite HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/UHF_LITE_HAT_EUROPE_VERSION_01.png?v=1676359993&width=700)
* [RFID HAT for RaspberryPi](https://shop.sb-components.co.uk/products/rfid-hat-for-raspberry-pi?_pos=3&_sid=59f725ea2&_ss=r)

 ![RFID HAT for RaspberryPi](https://cdn.shopify.com/s/files/1/1217/2104/products/RFIDforPi.jpg?v=1614587676&width=400)

* [RaspberryPi Pico RFID Expansion](https://shop.sb-components.co.uk/products/raspberry-pi-pico-rfid-expansion?_pos=3&_sid=075681430&_ss=r)

 ![RaspberryPi Pico RFID Expansion](https://cdn.shopify.com/s/files/1/1217/2104/products/2_85a5dfb2-96cb-4e0b-ba28-a70af127a4f1.png?v=1613732653&width=400)
 
* [UHF HAT For Raspberry-Pi](https://shop.sb-components.co.uk/products/uhf-hat-for-raspberry-pi?_pos=1&_sid=4a8407538&_ss=r)

 ![UHF HAT For Rpi](https://cdn.shopify.com/s/files/1/1217/2104/products/UHFHATForRaspberryPi.png?v=1648192425&width=400)
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
