# targeted-ad-iot

Requirements are in requirements.txt

image_pub.py captures frames using opencv, converts them into bytearrays and publishes to broker under topic 'face/cam1'
After an image is received by image_sub.py trained models are used to detect faces, extract gender and age information.
Information is then published to the broker under topic 'face/val', image capturing device receives this information and prints it.

Every time a new instance of cam_client is initialized the handler will assign it a unique id and deploy a container with that unique id.
docker_runner.bat file is used to deploy the docker container, at the moment system only works on windows machines however simply changin the batch script to a bash one will fix this issue.

Be sure to change the docker image name in docker_runner.bat after building it.

"test.mosquitto.org" broker is used, change for local broker.
