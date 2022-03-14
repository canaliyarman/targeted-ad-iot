FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY gender_deploy.prototxt gender_deploy.prototxt
COPY gender_net.caffemodel gender_net.caffemodel
COPY age_deploy.prototxt age_deploy.prototxt
COPY age_net.caffemodel age_net.caffemodel
COPY opencv_face_detector_uint8.pb opencv_face_detector_uint8.pb
COPY opencv_face_detector.pbtxt opencv_face_detector.pbtxt
COPY img_processing.py img_processing.py
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
ENTRYPOINT [ "python3", "-u" ,"img_processing.py" ]