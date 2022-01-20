# Complete project details at https://RandomNerdTutorials.com
from senko import senko
import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'LittleBird_Private'
password = 'LBRocks!IoT'

routercon = network.WLAN(network.STA_IF)
routercon.active()
routercon.active(True)
routercon.connect(ssid,password)
routercon = network.WLAN(network.STA_IF)

print('Connection successful')

#This part goes to github https://github.com/quintajm/SenkoTest and syncronizes with the repo on boot
OTA = senko.Senko(user = "quintajm",
                  repo="Fob-Test-ESp8266",
                  branch="main",
                  working_dir="Micropython",
                  files = ["boot.py","main.py","servo_control.py"]
                  )
print("Syncronization configured")

if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()
