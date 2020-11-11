from mqtt import MQTTClient
import machine, time, ujson

class Broker():
    def __init__(self):
        self.ip, self.client_id, self.topic, self.msg = self.getJsonInfo()
        self.client = MQTTClient(self.client_id, self.ip)
        time.sleep(3)
        self.client.connect()

    def objectDetected(self):
        self.client.publish(self.topic, self.msg)

    def getJsonInfo(self):
        with open("settings.json") as file:
            data = ujson.loads(file.read())
        return (data["brokerIp"], data["clientId"], data["topic"], data["msg"])

