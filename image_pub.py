import paho.mqtt.publish as publish
import cv2
import time

while True:
    cap = cv2.VideoCapture(0)
    hasFrame, frame = cap.read()
    aaa = "bok"
    publish.single('topic', aaa, qos=1, hostname='m2m.eclipse.org')
    time.sleep(1)