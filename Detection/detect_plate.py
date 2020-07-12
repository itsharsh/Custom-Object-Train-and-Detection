import cv2
import numpy as np
import os
import re
import time
import tensorflow as tf
#from datetime import datetime

import path_config
from DB import create_CSV



cfgfile = path_config.configFilePath
class_name = path_config.namesFilePath
tfweightfile = path_config.tfWeightFile
weightfile=path_config.weightsFilePath


cameraSource = path_config.cameraSource
#videoPath = path_config.originalVideoDir
videoPath= "/home/ai-ctrl/Aj___/Projectss/v3realtime/walking.mp4"
processedVideoDir=path_config.processedVideoDir
makeDirectoryCommand = "mkdir -p \"{}\"".format(processedVideoDir)
os.system(makeDirectoryCommand)
Streams = len(cameraSource)





#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("Hikvision License Plate Recognition (LPR) Camera Demo Video.mp4")
#cap= cv2.VideoCapture("/home/ai-ctrl/Aj___/Projectss/v3realtime/VID_20200125_163854.mp4")


for i in range(Streams):
    if type(cameraSource[i]) == str:
        exec("class run"+str(i)+"():\n\t"
# Load LicencePlate Detector
             "net = cv2.dnn.readNet(weightfile,cfgfile)\n\t"
             "classes = []\n\t"
             "with open(class_name, \"r\") as f:\n\t\t"
                 "classes = [line.strip() for line in f.readlines()]\n\t"
             "layer_names = net.getLayerNames()\n\t"
             "output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]\n\t"
             "colors = np.random.uniform(0, 255, size=(len(classes), 3))\n\t"

#read video
             "cam = cv2.VideoCapture(videoPath)\n\t" 
             "font = cv2.FONT_HERSHEY_PLAIN\n\t"
             "starting_time = time.time()\n\t"
             "frame_id = 0\n\t"
 
             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "while True:\n\t\t\t"
             "_, frame = cam.read()\n\t\t\t"
             "frame_id += 1\n\t\t\t"
             "height, width, channels = frame.shape\n\t\t\t"
             "print(frame.shape)\n\t\t\t"
# Detecting objects
             "blob = cv2.dnn.blobFromImage(frame, 0.00392, (608,608), (0, 0, 0), True, crop=False)\n\t\t\t"
 
             "net.setInput(blob)\n\t\t\t"
             "outs = net.forward(output_layers)\n\t\t\t"
 
# Showing informations on the screen
             "class_ids = []\n\t\t\t"
             "confidences = []\n\t\t\t"
             "boxes = []\n\t\t\t"
             "for out in outs:\n\t\t\t\t"
             "for detection in out:\n\t\t\t\t\t"
             "scores = detection[5:]\n\t\t\t\t\t"
             "class_id = np.argmax(scores)\n\t\t\t\t\t"
             "confidence = scores[class_id]\n\t\t\t\t\t"
             "if confidence > 0.2:\n\t\t\t\t\t\t"
# Object detected
             "center_x = int(detection[0] * width)\n\t\t\t\t\t\t"
             "center_y = int(detection[1] * height)\n\t\t\t\t\t\t"
             "w = int(detection[2] * width)\n\t\t\t\t\t\t"
             "h = int(detection[3] * height)\n\t\t\t\t\t\t"
# Rectangle coordinates
             "x = int(center_x - w / 2)\n\t\t\t\t\t\t"
             "y = int(center_y - h / 2)\n\t\t\t\t\t\t"

             "boxes.append([x, y, w, h])\n\t\t\t\t\t\t"
             "confidences.append(float(confidence))\n\t\t\t\t\t\t"
             "class_ids.append(class_id)\n\t\t\t"
 
             "indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.8, 0.3)\n\t\t\t"
 
             "for i in range(len(boxes)):\n\t\t\t\t"
             "if i in indexes:\n\t\t\t\t\t"
             "x, y, w, h = boxes[i]\n\t\t\t\t\t"
             "label = str(classes[class_ids[i]])\n\t\t\t\t\t"
             "confidence = confidences[i]\n\t\t\t\t\t"
             "color = colors[class_ids[i]]\n\t\t\t\t\t"
             "cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)\n\t\t\t\t\t"
#            cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + w/), font, 1, color, 1)
             "for i in indexes:\n\t\t\t\t\t\t"
             "cropped = frame[y:y+h , x:x+w]\n\t\t\t\t\t\t"
#            cv2.imwrite("crop.jpg",cropped)
#cv2.imshow("orig",img)
 
# Adding OCR
#    img = cv2.imread('crop.jpg')#Alternatively: can be skipped if you have a Blackwhite image
             "gray = cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)\n\t\t\t\t\t\t"
             "gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)\n\t\t\t\t\t\t"
             "gray = cv2.bitwise_not(img_bin)\n\t\t\t\t\t\t"
 
             "kernel = np.ones((2, 1), np.uint8)\n\t\t\t\t\t\t"
#img = cv2.erode(gray, kernel, iterations=1)
             "cropped = cv2.dilate(cropped, kernel, iterations=1)\n\t\t\t\t\t\t"
             "out_below = pytesseract.image_to_string(cropped)\n\t\t\t\t\t\t"
             "print(out_below)\n\t\t\t\t\t\t"
 
             "cv2.putText(frame, out_below,(x,y-w), font, 4, (0, 0, 0), 3)\n\t\t\t\t\t\t"
                                 
#cv2.imshow("crop",cropped)
             "elapsed_time = time.time() - starting_time\n\t\t\t\t\t"
             "fps = frame_id / elapsed_time\n\t\t\t\t\t"
#"cv2.putText(frame, "+str(FPS)+" +str(round(fps, 2)), (10, 50), font, 4, (0, 0, 0), 3)\n\t\t\t\t\t"
 
 
             "_, img2 = cv2.imencode(\".jpg\", frame)\n\t\t\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t\t\t"
            "yield img2\n\t"



             "@staticmethod\n\t"
             "def raw():\n\t\t"
             "while 1:\n\t\t\t"
             "ret, frame = run"+str(i)+".cam.read()\n\t\t\t"
             "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
             "yield img1.tobytes()\n\n")

    else:
        exec("class run"+str(i)+"():\n\t"
         "net = cv2.dnn.readNet(weightfile,cfgfile)\n\t"


         "classes = []\n\t"
         "with open(class_name, \"r\") as f:\n\t\t"
         "classes = [line.strip() for line in f.readlines()]\n\t"
         "layer_names = net.getLayerNames()\n\t"
         "output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]\n\t"
         "colors = np.random.uniform(0, 255, size=(len(classes), 3))\n\t"

         "cam = cv2.VideoCapture(cameraSource["+str(i)+"])\n\t" 
         "font = cv2.FONT_HERSHEY_PLAIN\n\t"
         "starting_time = time.time()\n\t"
         "frame_id = 0\n\t"

         "@staticmethod\n\t"
         "def processed():\n\t\t"
         "while True:\n\t\t\t"
         "_, frame = cam.read()\n\t\t\t"
         "frame_id += 1\n\t\t\t"
         "height, width, channels = frame.shape\n\t\t\t"
         "print(frame.shape)\n\t\t\t"
# Detecting objects
         "blob = cv2.dnn.blobFromImage(frame, 0.00392, (608,608), (0, 0, 0), True, crop=False)\n\t\t\t"

         "net.setInput(blob)\n\t\t\t"
         "outs = net.forward(output_layers)\n\t\t\t"

# Showing informations on the screen
         "class_ids = []\n\t\t\t"
         "confidences = []\n\t\t\t"
         "boxes = []\n\t\t\t"
         "for out in outs:\n\t\t\t\t"
         "for detection in out:\n\t\t\t\t\t"
         "scores = detection[5:]\n\t\t\t\t\t"
         "class_id = np.argmax(scores)\n\t\t\t\t\t"
         "confidence = scores[class_id]\n\t\t\t\t\t"
         "if confidence > 0.2:\n\t\t\t\t\t\t"
# Object detected
         "center_x = int(detection[0] * width)\n\t\t\t\t\t\t"
         "center_y = int(detection[1] * height)\n\t\t\t\t\t\t"
         "w = int(detection[2] * width)\n\t\t\t\t\t\t"
         "h = int(detection[3] * height)\n\t\t\t\t\t\t"

# Rectangle coordinates
         "x = int(center_x - w / 2)\n\t\t\t\t\t\t"
         "y = int(center_y - h / 2)\n\t\t\t\t\t\t"

         "boxes.append([x, y, w, h])\n\t\t\t\t\t\t"
         "confidences.append(float(confidence))\n\t\t\t\t\t\t"
         "class_ids.append(class_id)\n\t\t\t"

         "indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.8, 0.3)\n\t\t\t"

         "for i in range(len(boxes)):\n\t\t\t\t"
         "if i in indexes:\n\t\t\t\t\t"
         "x, y, w, h = boxes[i]\n\t\t\t\t\t"
         "label = str(classes[class_ids[i]])\n\t\t\t\t\t"
         "confidence = confidences[i]\n\t\t\t\t\t"
         "color = colors[class_ids[i]]\n\t\t\t\t\t"
         "cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)\n\t\t\t\t\t"
#            cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + w/), font, 1, color, 1)
         "for i in indexes:\n\t\t\t\t\t\t"
         "cropped = frame[y:y+h , x:x+w]\n\t\t\t\t\t\t"

# Adding OCR
#    img = cv2.imread('crop.jpg')#Alternatively: can be skipped if you have a Blackwhite image
         "gray = cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)\n\t\t\t\t\t\t"
         "gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)\n\t\t\t\t\t\t"
         "gray = cv2.bitwise_not(img_bin)\n\t\t\t\t\t\t"

         "kernel = np.ones((2, 1), np.uint8)\n\t\t\t\t\t\t"
#img = cv2.erode(gray, kernel, iterations=1)
         "cropped = cv2.dilate(cropped, kernel, iterations=1)\n\t\t\t\t\t\t"
         "out_below = pytesseract.image_to_string(cropped)\n\t\t\t\t\t\t"
         "print(out_below)\n\t\t\t\t\t\t"

         "cv2.putText(frame, out_below,(x,y-w), font, 4, (0, 0, 0), 3)\n\t\t\t\t\t\t"
                            

         "elapsed_time = time.time() - starting_time\n\t\t\t\t\t"
         "fps = frame_id / elapsed_time\n\t\t\t\t\t"
#"cv2.putText(frame, "+str(FPS)+" +str(round(fps, 2)), (10, 50), font, 4, (0, 0, 0), 3)\n\t\t\t\t\t"


         "_, img2 = cv2.imencode(\".jpg\", frame)\n\t\t\t\t\t"
         "img2 = img2.tobytes()\n\n\t\t\t\t\t"

         "yield img2\n\t"
                

         "@staticmethod\n\t"
         "def raw():\n\t\t\t"
         "while 1:\n\t\t\t\t"
         "ret, frame = run"+str(i)+".cam.read()\n\t\t\t\t"
         "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t\t"
         "yield img1.tobytes()\n\n")


def run():
    for i in range(Streams):
        exec("run"+str(i)+"()")


if __name__ == '__main__':
    run()
