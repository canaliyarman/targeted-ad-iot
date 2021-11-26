import paho.mqtt.client as mqtt
import cv2
from time import sleep

def getImage():
    cap = cv2.VideoCapture(0)
    hasFrame, frame = cap.read()
    if frame.shape[0] < 100:
        return
    image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
    message = client.publish("face/cam", image_bytes)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("face/val1")

    

def on_message(client, userdata, message,):
    print(str(message.payload))
    

def on_publish(client,userdata,result):
    print("sending image")

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("test_camera_device")
client.connect(mqttBroker,1883,60)
client.on_publish = on_publish
client.on_message = on_message
client.on_connect = on_connect
client.subscribe("face/val")

while True:
    client.loop()
    getImage()
