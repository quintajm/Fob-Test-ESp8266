import time
from umqtt.simple import MQTTClient
from machine import Pin, Timer

def sendHit(a):
    server = '10.0.0.211'
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"reader1", b"OK_Read")
    c.ping()
    c.disconnect()

def sendFail():
    server = '10.0.0.211'
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"reader1", b"Failed_Test")
    c.disconnect()

def SwitchState(state):
    return print("boom")

#Create timer for Failed test 
#tim = Timer(-1)
#tim.init(period=10000, mode=Timer.ONE_SHOT, callback=SwitchState)

# Create interrupt to read
read_pin = 12  # D6
pir = Pin(read_pin, Pin.IN)
pir.irq(trigger=Pin.IRQ_RISING, handler=sendHit) #The handler passes on the pin number automatically, so it returns an error. To avoid this add a var to the callback.

#Testing cycle
led = Pin(2, Pin.OUT) #Gpio that controls onboard LED
i = 0
timeout =time.time() + 60*5 #5 minute timeout
while True:
    time.sleep(2)
    led.value(0)
    i += 1
    print("Test cycle:{}".format(i))
    time.sleep(2)
    led.value(1)
    if i == 1000 or time.time() > timeout:
        break

sendFail()
    
    
