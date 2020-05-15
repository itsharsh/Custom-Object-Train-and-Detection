import os
import cv2
from flask import Flask, Response

from Camera import detect_camera

app = Flask("SAS")

host = "localhost"
port = 8080


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


for i in range(detect_camera.Streams):
    exec("@app.route(\"/camera"+str(i)+"\")\n"
         "def camera"+str(i)+"():\n\t"
         "return Response(gen0(detect_camera.run" +
         str(i)+".raw()),\n\t\t\t\t\t"
         "mimetype=\"multipart/x-mixed-replace; boundary=frame\")\n")

    exec("@app.route(\"/cameraprocessed"+str(i)+"\")\n"
         "def cameraprocessed"+str(i)+"():\n\t"
         "return Response(gen1(detect_camera.run" +
         str(i)+".processed()),\n\t\t\t\t\t"
         "mimetype=\"multipart/x-mixed-replace; boundary=frame\")\n")


def run():
    app.run(host=host, threaded=True, port=port)


if __name__ == '__main__':
    run()
