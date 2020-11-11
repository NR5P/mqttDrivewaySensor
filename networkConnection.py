import network, ujson

class NetworkConnection():
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def do_connect(self):
        if not self.wlan.isconnected():
            print('connecting to network...')
            essid, password = self._getWifiCreds()
            self.wlan.connect(essid, password)
            while not self.wlan.isconnected():
                pass
        print('network config:', self.wlan.ifconfig())

    def _getWifiCreds(self):
        with open("settings.json") as file:
            data = ujson.loads(file.read())
        return (data["ssid"], data["password"])

    def isConnected(self):
        return self.wlan.isconnected()