from mqtt import MQTTClient
import machine, time, ujson

class Broker():
    def __init__(self):
        self.ip, self.client_id, self.topic, self.msg = self.getJsonInfo()
        self.client = MQTTClient(self.client_id, self.ip, keepalive=3600*2)
        self.client.set_last_will(MQTT_STATUS_TOPIC, 'disconnected', retain=True)
        time.sleep(3)
        self.client.connect()

    def objectDetected(self):
        print("object detected, publishing")
        self.client.publish(self.topic, self.msg)

    def getJsonInfo(self):
        with open("settings.json") as file:
            data = ujson.loads(file.read())
        return (data["brokerIp"], data["clientId"], data["topic"], data["msg"])

