import machine

#Defaults to servo signal at D5
def setup(pin=14):
    signalPin = machine.Pin(pin)
    servo = machine.PWM(signalPin,freq=50)
    return servo

def forward(duty=40):
    servo = setup()
    servo.duty(duty)

def backwards(duty=115):
    servo = setup()
    servo.duty(duty)