import paho.mqtt.client as mqtt
import cv2
import time

mqttBroker = "192.168.1.102"
client = mqtt.Client("test_producer")
client.connect(mqttBroker,1883,60)
client.subscribe("test")
while True:
    cap = cv2.VideoCapture(0)
    hasFrame, frame = cap.read()
    image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
    message = client.publish("test", image_bytes)
    time.sleep(1)