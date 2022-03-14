import paho.mqtt.client as mqtt
import cv2
import advertisment
from time import sleep
import requests
import atexit


r = requests.get('http://127.0.0.1:5000/handle')

data = r.json()
topic = data['topic']
print(topic)

def exit_handler():
    print("Exiting")
    message = client.publish("face/cam/" + topic, "exit")


# Capture image from camera
def getImage():
    cap = cv2.VideoCapture(0)
    hasFrame, frame = cap.read()
    
    # If captured image is malfored return
    if frame.shape[0] < 100:
        return

    # Convert numpy array to byte array
    image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
    message = client.publish("face/cam/" + topic, image_bytes)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Connect to val topic to get response from published images
    client.subscribe("face/val/" + topic)

    

# Once a new val is published to topic
def on_message(client, userdata, message,):
    
    print(str(message.payload))
    temp = str(message.payload)

    if "no" not in temp:
        string = temp.split(" ")
        age = string[1]
        age = age.replace("'","")
        gender = string[0]
        gender = gender.replace("b'", "")

        # show add for the age-gender key
        advertisment.show_add(age, gender)



    
    

def on_publish(client,userdata,result):
    print("sending message")



# mosquitto's test broker open to anyone
mqttBroker = "test.mosquitto.org"
client = mqtt.Client("test_camera_device")
client.connect(mqttBroker,1883,60)
client.on_publish = on_publish
client.on_message = on_message
client.on_connect = on_connect
client.subscribe("face/val")
atexit.register(exit_handler)
# main loop
while True:
    client.loop()
    getImage()
