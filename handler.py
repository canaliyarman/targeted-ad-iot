import subprocess
from flask import Flask, jsonify, g
import uuid
import time
import os

#client = docker.from_env()
app = Flask(__name__)

def run_py(topic):
    #client.containers.run("94fa61e43f07", str(topic), detach=True)
    process = subprocess.Popen(['docker_runner.bat', str(topic)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.after_request
def run_img_processing(response):
    print(response)
    run_py(topic=g.topic)
    return response

@app.route('/handle', methods=['GET'])
def handle():
    topic = uuid.uuid4().hex
    g.topic = topic
    #run_py(topic=g.topic)
    return jsonify(topic=topic)

if __name__ == "__main__":
    app.run()