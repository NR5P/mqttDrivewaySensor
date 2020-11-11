import time, machine
from networkConnection import NetworkConnection
from motionDetector import MotionDetector
from broker import Broker

DETECTOR_PIN = 34

connection = NetworkConnection()
if connection.do_connect() == -1: # if there was an error connecting
    MotionDetector.sleep()
print("is connected: " + str(connection.isConnected()))
motionDetector = MotionDetector(DETECTOR_PIN)
broker = Broker()

if machine.wake_reason() == machine.PIN_WAKE:  # if woke by the motion sensor and not keep alive rtc timer
    broker.objectDetected()
else:
    print("just waking up to ping")

motionDetector.sleep()
    

