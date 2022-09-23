from utime import sleep_ms

try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

#The Onboard LED, used to show connection status
led = Pin(2, Pin.OUT)

#The Relay that sends the impules to the Door
relay = Pin(0, Pin.OUT)

#Set both the LED and relay to OFF 
led.value(1)
relay.value(1)

#Replace with your Wifi SSID and Password
ssid = 'XXXXXXX'
password = 'XXXXXXX'

wifi = network.WLAN(network.STA_IF)

#Connect to WiFi
def connectWifi():
    global wifi
    global led

    wifi.active(True)
    wifi.connect(ssid, password)

    while wifi.isconnected() == False:
        pass

    print('Connection successful')
    print(wifi.ifconfig())

    #Indicate that Wifi is connected with the on-board LED
    led.value(0)
    sleep_ms(200)
    led.value(1)
    sleep_ms(100)
    led.value(0)
    sleep_ms(200)
    led.value(1)
    sleep_ms(100)
    led.value(0)
    sleep_ms(200)
    led.value(1)

connectWifi()
