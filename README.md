# targeted-ad-iot

Requirements are in requirements.txt

image_pub.py captures frames using opencv, converts them into bytearrays and publishes to broker under topic 'face/cam1'
After an image is received by image_sub.py trained models are used to detect faces, extract gender and age information.
Information is then published to the broker under topic 'face/val', image capturing device receives this information and prints it.

"test.mosquitto.org" broker is used, change for local broker.
