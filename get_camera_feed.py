import cv2
import time
from datetime import datetime

ptzCameraSource = 0
camera1Source = "1.mp4"
camera2Source = "2.mp4"
camera3Source = "3.mp4"
camera4Source = "4.mp4"
camera5Source = "5.mp4"


class PTZCamera():
    camera = cv2.VideoCapture(ptzCameraSource)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = PTZCamera.camera.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(ptzCameraSource) is str):
                time.sleep(0.040)


class PTZCameraProcessed():
    camera = cv2.VideoCapture(ptzCameraSource)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = PTZCameraProcessed.camera.read()
            cv2.putText(frame, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3], (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(ptzCameraSource) is str):
                time.sleep(0.040)


class Camera1():
    camera = cv2.VideoCapture(camera1Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera1.camera.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera1Source) is str):
                time.sleep(0.040)


class Camera1Processed():
    camera = cv2.VideoCapture(camera1Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera1Processed.camera.read()
            cv2.putText(frame, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3], (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera1Source) is str):
                time.sleep(0.040)


class Camera2():
    camera = cv2.VideoCapture(camera2Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera2.camera.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera2Source) is str):
                time.sleep(0.040)


class Camera2Processed():
    camera = cv2.VideoCapture(camera2Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera2Processed.camera.read()
            cv2.putText(frame, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3], (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera2Source) is str):
                time.sleep(0.040)


class Camera3():
    camera = cv2.VideoCapture(camera3Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera3.camera.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera3Source) is str):
                time.sleep(0.040)


class Camera3Processed():
    camera = cv2.VideoCapture(camera3Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera3Processed.camera.read()
            cv2.putText(frame, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3], (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera3Source) is str):
                time.sleep(0.040)


class Camera4():
    camera = cv2.VideoCapture(camera4Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera4.camera.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera4Source) is str):
                time.sleep(0.040)


class Camera4Processed():
    camera = cv2.VideoCapture(camera4Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera4Processed.camera.read()
            cv2.putText(frame, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3], (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera4Source) is str):
                time.sleep(0.040)


class Camera5():
    camera = cv2.VideoCapture(camera5Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera5.camera.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera5Source) is str):
                time.sleep(0.040)


class Camera5Processed():
    camera = cv2.VideoCapture(camera5Source)
    @staticmethod
    def frames():
        while True:
            # read current frame
            _, frame = Camera5Processed.camera.read()
            cv2.putText(frame, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3], (10, 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()
            if(type(camera5Source) is str):
                time.sleep(0.040)
