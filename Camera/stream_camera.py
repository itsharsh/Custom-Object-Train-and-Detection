#!/usr/bin/env python
from Detection import detect_person
import webbrowser
from Camera import get_camera_feed
import cv2
import os
from importlib import import_module
from flask import Flask, render_template, Response


app = Flask("SAS")

host = "localhost"
port = 8888


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
