# ESP8266-GarageDoorOpener
Simple Garage door opener using an ESP8266-01S with a Relay module

This project works with Garage Doors that can handle one input for Open, Close and Stop.

For Garage Doors that have separate pins for the different operations, you need to adopt the code and add more relays and buttons for the different operations.

## How it works
This program starts a webserver that listens to requests.

The webserver serves a simple HTML page and a small embedded javascript.

The user interface consists of a large button.

When pressed, a request is done to /?operateDoor, which sends a short impulse by activating the relay for 500ms.

### LED Indicator

When the module successfully connects to Wifi, it will blink quickly three times.

When ready to recieve requests, it will blink every half second.

When the door is being operated, the led will be lit for half a second.

## Installation
Add both the boot.py and main.py to the ESP Module.

Set your SSID and Wifi password.

If you're using a different ESP8266 module or an ESP32, you might need to change which pins you are using for the LED and the Relay for it to work.

## Hooking it up to the Door Control Unit
My garage has one single impulse input, that toggles between Open / Stop / Close by connecting two inputs.

I connected one of the ports to COM on the relay and the other, through a 200 OHM resistor, to NO (Normally Open).

## My Setup
I'm using an ESP-01S with a relay module that I bought from AZ-Delivery. Other boards or relay modules should work as well, however, if you're using a different ESP8266 module or an ESP32, you might need to change which pins you are using for the LED and the Relay for it to work. This can be done in boot.py.

![AZ-Delivery ESP-01S With Relay Module](https://github.com/mannbro/ESP8266-GarageDoorOpener/raw/main/ESP8266-01S-Relay-Module.jpg)

## Security
Keep in mind that the webserver is not secured, which means that anyone connected to your Wifi can control the door.

Garage Doors are also heavy and in order to operate the door, you might expose 230V or 120V, which could be lethal.

Because of this, I can't recommend using this other than as a proof of concept unless you know what you're doing.

ALL USE IS AT YOUR OWN RISK.
