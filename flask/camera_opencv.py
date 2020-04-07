import cv2
#from base_camera import BaseCamera
import time


class Camera1():
    camera = cv2.VideoCapture(0)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, img = Camera1.camera.read()

            # encode as a jpeg image and return it
            _,jpeg=cv2.imencode('.jpg', img)
            yield jpeg.tobytes()

class Camera2():
    camera = cv2.VideoCapture('/home/vivek/O2i-SAS/flask/test.mp4')
    @staticmethod
    def frames():
        while True:
            # read current frame
            _,img = Camera2.camera.read()
            # encode as a jpeg image and return it
            _,jpeg=cv2.imencode('.jpg', img)
            yield jpeg.tobytes()
            time.sleep(0.040)
