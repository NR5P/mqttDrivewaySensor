import network, ujson, utime

class NetworkConnection():
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def do_connect(self):
        if not self.wlan.isconnected():
            print('connecting to network...')
            essid, password = self._getWifiCreds()
            self.wlan.connect(essid, password)
            connStartTime = utime.time()
            while not self.wlan.isconnected():
                if connStartTime - utime.time() > 10:
                    print("no wifi detected going back to sleep")
                    return
        print('network config:', self.wlan.ifconfig())

    def _getWifiCreds(self):
        with open("settings.json") as file:
            data = ujson.loads(file.read())
        return (data["ssid"], data["password"])

    def isConnected(self):
        return self.wlan.isconnected()

    def disconnect(self):
        self.wlan.disconnect()