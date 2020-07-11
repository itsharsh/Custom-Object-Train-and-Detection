import cv2
import os
import re
import time
import tensorflow as tf
#from datetime import datetime

import path_config
from DB import create_CSV

cameraSource = path_config.cameraSource
#videoPath = path_config.originalVideoDir
videoPath= "/home/ai-ctrl/Aj___/Projectss/v3realtime/walking.mp4"
processedVideoDir=path_config.processedVideoDir
makeDirectoryCommand = "mkdir -p \"{}\"".format(processedVideoDir)
os.system(makeDirectoryCommand)
Streams = len(cameraSource)

faceDetect=cv2.CascadeClassifier('/home/ai-ctrl/Downloads/frontal_face.xml')


for i in range(Streams):
    if type(cameraSource[i]) == str:
        exec("class run"+str(i)+"():\n\t"
             "cap=cv2.VideoCapture(videoPath)\n\t" 
             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "while True:\n\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t"
             "if not ret:\n\t\t\t\t"
             "break\n\n\t\t\t"
             "gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n\t\t\t"
             "faces = faceDetect.detectMultiScale(gray,1.2)\n\t\t\t"
             "for (x,y,w,h) in faces:\n\t\t\t\t"
                 "cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)\n\t\t\t"
                

             "_, img2 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t"

             "yield img2\n\n\t\t\t"

            
             "key = cv2.waitKey(1) & 0xFF\n\t\t\t"

             "if key == ord('q'):\n\t\t\t\t"
             "break\n\t"
             "@staticmethod\n\t"
             "def raw():\n\t\t\t"
             "while 1:\n\t\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t\t"
             "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t\t"
             "yield img1.tobytes()\n\n")



    else:
        exec("class run"+str(i)+"():\n\t"
             "cap=cv2.VideoCapture(cameraSource["+str(i)+"])\n\t" 
             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "while True:\n\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t"
             "if not ret:\n\t\t\t\t"
             "break\n\n\t\t\t"
             "gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n\t\t\t"
             "faces = faceDetect.detectMultiScale(gray,1.2)\n\t\t\t"
             "for (x,y,w,h) in faces:\n\t\t\t\t"
                 "cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)\n\t\t\t"
                

             "_, img2 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t"

             "yield img2\n\n\t\t\t"

            
             "key = cv2.waitKey(1) & 0xFF\n\t\t\t"

             "if key == ord('q'):\n\t\t\t\t"
             "break\n\t"
             "@staticmethod\n\t"
             "def raw():\n\t\t\t"
             "while 1:\n\t\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t\t"
             "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t\t"
             "yield img1.tobytes()\n\n")

#cam.release()
#cv2.destroyAllWindows()



def run():
    for i in range(Streams):
        exec("run"+str(i)+"()")


if __name__ == '__main__':
    run()
