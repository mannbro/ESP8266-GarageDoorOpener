# ESP8266-GarageDoorOpener
Simple Garage door opener using an ESP8266-01S with a Relay module

This project works with Garage Doors that can handle one input for Open, Close and Stop.

For Garage Doors that have separate pins for the different operations, you need to adopt the code and add more relays and buttons for the different operations.

## Installation
Add both the boot.py and main.py to the ESP Module.

Set your SSID and Wifi password.

If you're using a different ESP8266 or ESP32, you might need to change which pins you are using for the LED and the Relay.

## My Setup

![AZ-Delivery ESP-01S With Relay Module](https://github.com/mannbro/ESP8266-GarageDoorOpener/raw/main/ESP8266-01S-Relay-Module.jpg)

## Security
Keep in mind that the webserver is not secured, which means that anyone connected to your Wifi can control the door. Because of this, I can't recommend using this other than as a proof of concept. ALL USE IS AT YOUR OWN RISK.
