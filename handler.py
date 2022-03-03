import subprocess
from flask import Flask, jsonify, g
import uuid
import time
import os
app = Flask(__name__)

def run_py(topic):
    process = subprocess.Popen(['python', 'img_processing.py', str(topic)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.after_request
def run_img_processing(response):
    time.sleep(2)
    print(response)
    run_py(topic=g.topic)
    return response

@app.route('/handle', methods=['GET'])
def handle():
    topic = uuid.uuid4().hex
    g.topic = topic
    #run_py(topic=g.topic)
    return jsonify(topic=topic)

@app.route('/test', methods=['GET'])
def test():
    return jsonify('bok')
if __name__ == "__main__":
    app.run()