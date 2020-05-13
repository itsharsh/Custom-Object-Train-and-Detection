#!/usr/bin/env python
import os
from importlib import import_module
from flask import Flask, render_template, Response
<<<<<<< HEAD
import cv2

from Camera import get_camera_feed
=======
import webbrowser
#from Detection import detect_branding
#from Camera import get_camera_feed
from Detection import detect_person
>>>>>>> Test-detect

app = Flask("SAS")

host = "localhost"
<<<<<<< HEAD
port = 5540
=======
port = 80
>>>>>>> Test-detect


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('Stream.html')


def gen0(camera):
    """Video streaming generator function."""
    for img1 in camera:
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield img1
        yield b'\r\n\r\n'


def gen1(camera):
    """Video streaming generator function."""
    for img2 in camera:
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield img2
        yield b'\r\n\r\n'


@app.route('/camera0')
def camera0():
    return Response(gen0(detect_person.run.main1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/cameraprocessed0')
def cameraprocessed0():
    return Response(gen1(detect_person.run.main()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#    app.run(host=host, threaded=True, port=port)


def run():
    app.run(host=host, threaded=True, port=port)

if __name__ == '__main__':
    run()