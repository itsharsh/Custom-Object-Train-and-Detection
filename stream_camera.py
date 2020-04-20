#!/usr/bin/env python
import os
from importlib import import_module
from flask import Flask, render_template, Response
import webbrowser

import get_camera_feed

# Streams=int(input('Stream:'))

app = Flask("SAS")

host = "localhost"
port = 8888


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('Stream.html')


mimetype = 'multipart/x-mixed-replace; boundary=frame'


def gen(camera):
    """Video streaming generator function."""
    for frame in camera.frames():
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield frame
        yield b'\r\n\r\n'


for i in range(get_camera_feed.Streams):
    exec("@app.route(\"/camera"+str(i)+"\")\ndef camera"+str(i)+"():return Response(gen(get_camera_feed.Camera" +
         str(i)+"()),mimetype=\"multipart/x-mixed-replace; boundary=frame\")")


if __name__ == '__main__':
    app.run(host=host, threaded=True, port=port)
