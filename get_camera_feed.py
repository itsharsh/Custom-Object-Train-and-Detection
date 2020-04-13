import cv2
import time
from datetime import datetime
import path_config

videoPath=path_config.testVideos
Streams=int(input('Stream Classes:'))
cameraSource=path_config.cameraSource



for i in range(Streams):
    if type(cameraSource[i])==int:
        exec("class Camera"+str(i)+"():\n\tcamera=cv2.VideoCapture(cameraSource["+str(i)+"])\n\t@staticmethod\n\tdef frames():\n\t\twhile True:\n\t\t\t_, frame = Camera"+str(i)+".camera.read()\n\t\t\t_, jpeg = cv2.imencode(\".jpeg\", frame)\n\t\t\tyield jpeg.tobytes()\n\t\t\tif(type(cameraSource["+str(i)+"]) is str):\n\t\t\t\ttime.sleep(0.040)")
    else:
        exec("class Camera"+str(i)+"():\n\tcamera=cv2.VideoCapture(videoPath+cameraSource["+str(i)+"])\n\t@staticmethod\n\tdef frames():\n\t\twhile True:\n\t\t\t_, frame = Camera"+str(i)+".camera.read()\n\t\t\t_, jpeg = cv2.imencode(\".jpeg\", frame)\n\t\t\tyield jpeg.tobytes()\n\t\t\tif(type(cameraSource["+str(i)+"]) is str):\n\t\t\t\ttime.sleep(0.040)")