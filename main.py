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
broker.objectDetected()

motionDetector.sleep()
    

