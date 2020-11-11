import micropython
from machine import Pin

class MotionDetector():
    def __init__(self, pinNum):
        self.pin = Pin(pinNum, Pin.IN)

    def check(self):
        if self.pin.value() == 1:
            return True
        return False