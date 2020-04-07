#!/usr/bin/env python
import os
from importlib import import_module
from flask import Flask, render_template, Response

import get_camera_feed

app = Flask("SAS")

host = "localhost"
port = 8888


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('Stream.html')


def gen(camera):
    """Video streaming generator function."""
    for frame in camera.frames():
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield frame
        yield b'\r\n\r\n'


@app.route('/ptzcamera')
def ptzcamera():
    return Response(gen(get_camera_feed.PTZCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/ptzcameraprocessed')
def ptzcameraprocessed():
    return Response(gen(get_camera_feed.PTZCameraProcessed()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera1')
def camera1():
    return Response(gen(get_camera_feed.Camera1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera1processed')
def camera1processed():
    return Response(gen(get_camera_feed.Camera1Processed()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera2')
def camera2():
    return Response(gen(get_camera_feed.Camera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera2processed')
def camera2processed():
    return Response(gen(get_camera_feed.Camera2Processed()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera3')
def camera3():
    return Response(gen(get_camera_feed.Camera3()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera3processed')
def camera3processed():
    return Response(gen(get_camera_feed.Camera3Processed()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera4')
def camera4():
    return Response(gen(get_camera_feed.Camera4()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera4processed')
def camera4processed():
    return Response(gen(get_camera_feed.Camera4Processed()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera5')
def camera5():
    return Response(gen(get_camera_feed.Camera5()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera5processed')
def camera5processed():
    return Response(gen(get_camera_feed.Camera5Processed()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host=host, threaded=True, port=port)
