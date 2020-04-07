#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
import webbrowser
url = 'http://0.0.0.0:8888/'

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

chrome_path = '/usr/bin/google-chrome %s'

# import camera driver
'''
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera
'''
#
from camera_opencv import Camera1, Camera2


app = Flask(__name__)


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


@app.route('/video_feed1')
def video_feed1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


webbrowser.get(chrome_path).open(url)



if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=8888)
    