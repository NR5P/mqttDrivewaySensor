import time
from networkConnection import NetworkConnection
from motionDetector import MotionDetector
from broker import Broker

DETECTOR_PIN = 34

connection = NetworkConnection()
connection.do_connect()
print("is connected: " + str(connection.isConnected()))
motionDetector = MotionDetector(DETECTOR_PIN)
broker = Broker()

while True:
    time.sleep(1)
    if not connection.isConnected():
        connection.do_connect()
    if motionDetector.check() == True:
        broker.objectDetected()
    

