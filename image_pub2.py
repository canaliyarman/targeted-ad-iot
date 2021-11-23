import paho.mqtt.client as mqtt
import cv2
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("face/val2")

def on_message(client, userdata, message,):
    print(str(message.payload))

def on_publish(client,userdata,result):
    pass

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("test_camera_device")
client.connect(mqttBroker,1883,60)
client.on_publish = on_publish
client.on_message = on_message
client.on_connect = on_connect
while True:
    cap = cv2.VideoCapture(0)
    hasFrame, frame = cap.read()
    image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
    message = client.publish("face/cam2", image_bytes)
    client.loop()