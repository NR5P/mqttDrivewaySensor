import micropython, esp32
import machine

class MotionDetector():
    def __init__(self, pinNum):
        self.pin = machine.Pin(pinNum, machine.Pin.IN)

    def check(self):
        if self.pin.value() == 1:
            return True
        return False

    def sleep(self):
        esp32.wake_on_ext0(pin = self.pin, level = esp32.WAKEUP_ANY_HIGH)
        machine.deepsleep(3600000)

