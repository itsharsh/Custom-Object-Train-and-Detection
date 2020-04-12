import cv2
import time
from datetime import datetime

Streams=int(input('Stream Classes:'))

camera0Source = "/home/vivek/AdTracker/test1.mp4"
camera1Source = "/home/vivek/AdTracker/test2.mp4"
camera2Source = "/home/vivek/AdTracker/test3.mp4"
camera3Source = "/home/vivek/AdTracker/test4.mp4"
camera4Source = "/home/vivek/AdTracker/test5.mp4"
camera5Source = "/home/vivek/AdTracker/test6.mp4"

camera6Source = "/home/vivek/AdTracker/test7.mp4"
camera7Source = "/home/vivek/AdTracker/test8.mp4"
camera8Source = "/home/vivek/AdTracker/test9.mp4"
camera9Source = "/home/vivek/AdTracker/test10.mp4"
camera10Source = "/home/vivek/AdTracker/test11.mp4"
camera11Source = "/home/vivek/AdTracker/test12.mp4"


for i in range(Streams):
    exec("class Camera"+str(i)+"():\n\tcamera=cv2.VideoCapture(camera"+str(i)+"Source)\n\t@staticmethod\n\tdef frames():\n\t\twhile True:\n\t\t\t_, frame = Camera"+str(i)+".camera.read()\n\t\t\t_, jpeg = cv2.imencode(\".jpeg\", frame)\n\t\t\tyield jpeg.tobytes()\n\t\t\tif(type(camera"+str(i)+"Source) is str):\n\t\t\t\ttime.sleep(0.040)")
