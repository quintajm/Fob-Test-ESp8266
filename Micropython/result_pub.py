from umqtt.simple import MQTTClient

def sendHit():
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