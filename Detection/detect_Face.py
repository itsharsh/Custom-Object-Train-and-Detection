import cv2
import csv
import numpy as np
import os
import re
import time
#import tensorflow as tf
#from datetime import datetime
import path_config
from DB import create_CSV



#openvino_modelDir =path_config.configFilePath
cfgfile = path_config.binFilePath
weightfile = path_config.xmlFilePath

cameraSource = path_config.cameraSource
#videoPath = path_config.originalVideoDir
#videoPath= "/home/ai-ctrl/Aj___/Projectss/v3realtime/walking.mp4"

videoPath = "/home/ai-ctrl/Aj___/Office/gitrepository/SAS/head-pose-face-detection-female.mp4"
#processedVideoDir=path_config.processedVideoDir
#makeDirectoryCommand = "mkdir -p \"{}\"".format(processedVideoDir)
#os.system(makeDirectoryCommand)
Streams = len(cameraSource)
file = "/home/ai-ctrl/Documents/cordfile.csv"


net = cv2.dnn.readNet(weightfile,cfgfile)
# Load the faceLandmarksDetector
#net = cv.dnn.readNet('/home/ai-ctrl/Aj___/Projectss/myvinoproject/myvinoproject2/facial-landmarks-35-adas-0002.xml','/home/ai-ctrl/Aj___/Projectss/myvinoproject/myvinoproject2/facial-landmarks-35-adas-0002.bin')


# Specify target device
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("Hikvision License Plate Recognition (LPR) Camera Demo Video.mp4")
#cap= cv2.VideoCapture("/home/ai-ctrl/Aj___/Projectss/v3realtime/VID_20200125_163854.mp4")


for i in range(Streams):
    if type(cameraSource[i]) == str:
        exec("class run"+str(i)+"():\n\t"
             "cam = cv2.VideoCapture(videoPath)\n\t" 
             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "while True:\n\t\t\t"
             "ret, frame= run"+str(i)+".cam.read()\n\t\t\t"
             "if not ret:\n\t\t\t\t"
                 "break\n\t\t\t"



        # Prepare input blob and perform an inference
             "blob = cv2.dnn.blobFromImage(frame, size=(672, 384), ddepth=cv2.CV_8U)\n\t\t\t"
             "net.setInput(blob)\n\t\t\t"
             "out = net.forward()\n\t\t\t"
#             "print(out)\n\t\t\t"

                # Draw detected faces on the frame
             "for detection in out.reshape(-1, 7):\n\t\t\t\t"
#    print(detection)
             "confidence = float(detection[2])\n\t\t\t\t"
             "xmin = int(detection[3] * frame.shape[1])\n\t\t\t\t"
             "ymin = int(detection[4] * frame.shape[0])\n\t\t\t\t"
             "xmax = int(detection[5] * frame.shape[1])\n\t\t\t\t"
             "ymax = int(detection[6] * frame.shape[0])\n\t\t\t\t"
             "if confidence > .5:\n\t\t\t\t\t"
             "cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))\n\t\t\t\t"
             "if os.path.exists(file):\n\t\t\t\t\t"

                 "cords = []\n\t\t\t\t\t"

                 "with open(file, 'r') as csvfile:\n\t\t\t\t\t\t"
                     "print(\"opening File\")\n\t\t\t\t\t\t"
                     "csvreader = csv.reader(csvfile)\n\t\t\t\t\t\t"
                     "for row in csvreader:\n\t\t\t\t\t\t\t"
                         "print(row)\n\t\t\t\t\t\t\t"
                         "cords.append(row)\n\t\t\t\t\t\t"
                    
#                    print(cords)
                     "xCord = int(cords[-1][0])\n\t\t\t\t\t\t"
                     "yCord = int(cords[-1][1])\n\t\t\t\t\t\t"
                     #"print("xCord{}  yCord {}".format(xCord,yCord))
#                    plr = cpt
#                    cpt += 1
                     "if xmin < xCord > xmax and ymin < yCord > ymax:\n\t\t\t\t\t\t\t"
                         "print(\"face_present\")\n\t\t\t\t\t\t\t"
                         "cropped = frame[ymin:ymax,xmin:xmax]\n\t\t\t\t\t\t\t"
                         "print(\"gett croppped portion\")\n\t\t\t\t\t\t\t"
                         "timestr = time.strftime(\"%Y%m%d-%H%M%S\")\n\t\t\t\t\t\t\t"
                         "cropFace = cv2.imwrite(\"im%s_L.jpg\" %timestr, cropped)\n\t\t\t\t\t\t\t"
                        #"cropFace = cv2.imwrite(\"im%s_L.jpg\" %timestr,frame[ymin:ymax,xmin:xmax])\n\t\t\t\t\t\t\t"
                         "cv2.imshow(\"cropFace\",cropFace)\n\t\t\t\t\t\t\t"
                         "print(\"written cropface image\")\n\t\t\t\t\t\t\t"
                         "os.remove(file)\n\t\t\t"


                # Save the frame to an image file
        #    cv.imwrite('outjj.png', frame) 
         #    "cv2.startWindowThread()\n\t\t\t"
          #   "cv2.namedWindow(\"preview\")\n\t\t\t"
           #  "cv2.imshow(\"preview\", frame)\n\t\t\t"
             "_, img2 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
             "img2 = img2.tobytes()\n\t\t\t"
             "yield img2\n\t"

             "@staticmethod\n\t"
             "def raw():\n\t\t"
             "while True:\n\t\t\t"
             "ret, frame= run"+str(i)+".cam.read()\n\t\t\t"
             "if not ret:\n\t\t\t\t"
             "break\n\t\t\t"
             "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
             "img1 = img1.tobytes()\n\t\t\t"
             "yield img1\n")

    else:
        exec("class run"+str(i)+"():\n\t"
             "cam=cv2.VideoCapture(cameraSource["+str(i)+"])\n\t" 
             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "while True:\n\t\t\t"
             "ret, frame= run"+str(i)+".cam.read()\n\t\t\t"
             "if not ret:\n\t\t\t\t"
                 "break\n\t\t\t"



        # Prepare input blob and perform an inference
             "blob = cv2.dnn.blobFromImage(frame, size=(672, 384), ddepth=cv2.CV_8U)\n\t\t\t"
             "net.setInput(blob)\n\t\t\t"
             "out = net.forward()\n\t\t\t"
#             "print(out)\n\t\t\t"

                # Draw detected faces on the frame
             "for detection in out.reshape(-1, 7):\n\t\t\t\t"
#    print(detection)
             "confidence = float(detection[2])\n\t\t\t\t"
             "xmin = int(detection[3] * frame.shape[1])\n\t\t\t\t"
             "ymin = int(detection[4] * frame.shape[0])\n\t\t\t\t"
             "xmax = int(detection[5] * frame.shape[1])\n\t\t\t\t"
             "ymax = int(detection[6] * frame.shape[0])\n\t\t\t\t"
             "if confidence > .5:\n\t\t\t\t\t"
             "cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))\n\t\t\t\t"
             "if os.path.exists(file):\n\t\t\t\t\t"
                 "cords = []\n\t\t\t\t\t"
                 "with open(file, 'r') as csvfile:\n\t\t\t\t\t\t"
                     "print(\"opening File\")\n\t\t\t\t\t\t"
                     "csvreader = csv.reader(csvfile)\n\t\t\t\t\t\t"
                     "for row in csvreader:\n\t\t\t\t\t\t\t"
                         "print(row)\n\t\t\t\t\t\t\t"
                         "cords.append(row)\n\t\t\t\t\t\t"
#                    print(cords)
                     "xCord = int(cords[-1][0])\n\t\t\t\t\t\t"
                     "yCord = int(cords[-1][1])\n\t\t\t\t\t\t"
                     "print(\"xmin: {} , xmax: {} , ymin: {}, ymax: {}\".format(xmin,xmax,ymin,ymax))\n\t\t\t\t\t\t"
                     #"print("xCord{}  yCord {}".format(xCord,yCord))
#                    plr = cpt
#                    cpt += 1
                     "if xmin < xCord > xmax and ymin < yCord > ymax:\n\t\t\t\t\t\t\t"
                         "print(\"face_present\")\n\t\t\t\t\t\t\t"
                         "cropped = frame[ymin:ymax,xmin:xmax]\n\t\t\t\t\t\t\t"
                         "print(\"cropped\")\n\t\t\t\t\t\t\t"
                         "timestr = time.strftime(\"%Y%m%d-%H%M%S\")\n\t\t\t\t\t\t\t"
                         "cropFace = cv2.imwrite(\"im%s_L.jpg\" %timestr,cropped)\n\t\t\t\t\t\t\t"
                         "cv2.imshow(\"cropFace\",cropFace)\n\t\t\t\t\t\t\t"
                         "print(\"written cropface image\")\n\t\t\t\t\t\t\t"
                         "os.remove(file)\n\t\t\t"



                # Save the frame to an image file
        #    cv.imwrite('outjj.png', frame) 
         #    "cv2.startWindowThread()\n\t\t\t"
          #   "cv2.namedWindow(\"preview\")\n\t\t\t"
           #  "cv2.imshow(\"preview\", frame)\n\t\t\t"
             "_, img2 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t"
             "yield img2\n\t"

             "@staticmethod\n\t"
             "def raw():\n\t\t"
             "while True:\n\t\t\t"
             "ret, frame= run"+str(i)+".cam.read()\n\t\t\t"
             "if not ret:\n\t\t\t\t"
             "break\n\t\t\t"
             "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
             "img1 = img1.tobytes()\n\t\t\t"
             "yield img1\n")


def run():
    for i in range(Streams):
        exec("run"+str(i)+"()")


if __name__ == '__main__':
    run()
