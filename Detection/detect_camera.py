import cv2
import os
import re
import time
import multiprocessing
import tensorflow as tf
from datetime import datetime

import path_config
from DB import create_CSV
from Model.yolov3 import utils
from Model.yolov3 import yolov3
from Model import convert_weights_tf

model_size = (352, 352, 3)
num_classes = 80
max_output_size = 100
max_output_size_per_class = 20
iou_threshold = 0.5
confidence_threshold = 0.5
frameRate=25


cfgfile = path_config.configFilePath
class_name = path_config.namesFilePath
weightfile = path_config.tfWeightFile

cameraSource = path_config.cameraSource
videoPath = path_config.originalVideoDir
processedVideoDir=path_config.processedVideoDir
makeDirectoryCommand = "mkdir -p \"{}\"".format(processedVideoDir)
os.system(makeDirectoryCommand)
Streams = len(cameraSource)

for i in range(Streams):
    if type(cameraSource[i]) == str:
        exec("class run"+str(i)+"():\n\t"

             "model = yolov3.YOLOv3Net(cfgfile, model_size, num_classes)\n\t"

             "try:\n\t\t"
             "model.load_weights(weightfile)\n\t"
             "except:\n\t\t"
             "convert_weights_tf.run()\n\t\t"
             "model.load_weights(weightfile)\n\t"

             "class_names = utils.load_class_names(class_name)\n\t"
              "cap = cv2.VideoCapture(os.path.join(videoPath,cameraSource["+str(i)+"]))\n\t"

             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "timeStamp = []\n\t\t"
             "crowdNum = []\n\t\t"
             "frameIndex = 0\n\t\t"
             "sourceFileName = []\n\t\t"    
             "classIndex = [None]*len(run"+str(i)+".class_names)\n\t\t"
             "classesName = []\n\t\t"
             "datetimeFormat = datetime.now().strftime(\"%Y/%m/%d-%H:%M:%S.%f\")[:-3]\n\t\t"
             "videoName=\"\".join(re.split(\"/|:\",datetimeFormat))\n\t\t"
             "videoName=\"\".join((videoName,\".mp4\"))\n\t\t"
             "frame_size = (int(run"+str(i)+".cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(run"+str(i)+".cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))\n\n\t\t"
             "videoWrite = cv2.VideoWriter(os.path.join(processedVideoDir,videoName),cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),frameRate,frame_size)\n\t\t"
             "start1 = time.perf_counter()\n\t\t"
             "detectInfo = []\n\n\t\t"

             "try:\n\t\t\t"
             "while True:\n\t\t\t\t"
             "start = time.time()\n\t\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t\t"
             "if not ret:\n\t\t\t\t\t"
             "break\n\n\t\t\t\t"

             "resized_frame = tf.expand_dims(frame, 0)\n\t\t\t\t"
             "resized_frame = utils.resize_image(resized_frame, (model_size[0], model_size[1]))\n\t\t\t\t"

             "pred = run" +
             str(i)+".model.predict(resized_frame)\n\t\t\t\t"

             "boxes, scores, classes, nums = utils.output_boxes(\n\t\t\t\t\t"
             "pred, model_size,\n\t\t\t\t\t"
             "max_output_size=max_output_size,\n\t\t\t\t\t"
             "max_output_size_per_class=max_output_size_per_class,\n\t\t\t\t\t"
             "iou_threshold=iou_threshold,\n\t\t\t\t\t"
             "confidence_threshold=confidence_threshold)\n\n\t\t\t\t"

             "img, getTime, persons, bboxes = utils.draw_outputs(\n\t\t\t\t\t"
             "frame, boxes, scores, classes, nums, run" +
             str(i)+".class_names)\n\t\t\t\t"
             "cv2.putText(img, datetime.now().strftime(\"%Y/%m/%d-%H:%M:%S.%f\")\n\t\t\t\t\t\t\t"
             "[:-3], (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)\n\t\t\t\t"
             "if getTime != 0:\n\t\t\t\t\t"
             "timeStamp.append(getTime)\n\t\t\t\t\t"
             "crowdNum.append(persons)\n\t\t\t\t\t"
             "sourceFileName.append(videoName.split(\".\")[0])\n\t\t\t\t\t"
             "if classIndex[0] is None:\n\t\t\t\t\t\t"
             "classIndex[0] = [frameIndex]\n\t\t\t\t\t"
             "else:\n\t\t\t\t\t\t"
             "classIndex[0].append(frameIndex)\n\n\t\t\t\t"
             "videoWrite.write(img)\n\n\t\t\t\t"

             "_, img2 = cv2.imencode(\".jpg\", img)\n\t\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t\t"

             "yield img2\n\n\t\t\t\t"

             "stop = time.time()\n\t\t\t\t"

             "seconds = stop - start\n\t\t\t\t"

             "fps = 1 / seconds\n\t\t\t\t"
             "print(\"Estimated frames per second : {0}\".format(fps))\n\t\t\t\t"
             "if frameIndex == 50:\n\t\t\t\t\t"
             "break\n\t\t\t\t"
             "frameIndex += 1\n\t\t\t\t"

             "key = cv2.waitKey(1) & 0xFF\n\t\t\t\t"

             "if key == ord('q'):\n\t\t\t\t\t"
             "break\n\t\t"
             "finally:\n\t\t\t"
             "cv2.destroyAllWindows()\n\t\t\t"
                    "run"+str(i)+".cap.release()\n\t\t\t"
                    "videoWrite.release()\n\t\t\t"
                    "print('Detections have been performed successfully.')\n\t\t"
             "end1 = time.perf_counter()-start1\n\t\t"
             "print(\"finish\", end1)\n\t\t"
             "print(\"Count\", frameIndex)\n\t\t"
             "num_processes = multiprocessing.cpu_count()\n\t\t"
             "print(\"Number of CPU: \" + str(num_processes))\n\t\t"

             "detectInfo = {\"Index\": classIndex,\"crowd\": crowdNum, \"time\": timeStamp, \"Source File\": sourceFileName}\n\t\t"

             "create_CSV.update(detectInfo)\n\t"

             "@staticmethod\n\t"
             "def raw():\n\t\t"
             "while 1:\n\t\t\t"
                    "ret, frame = run"+str(i)+".cap.read()\n\t\t\t"
                    "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
                    "yield img1.tobytes()\n\n")

    else:
        exec("class run"+str(i)+"():\n\t"

             "model = yolov3.YOLOv3Net(cfgfile, model_size, num_classes)\n\t"

             "try:\n\t\t"
             "model.load_weights(weightfile)\n\t"
             "except:\n\t\t"
             "convert_weights_tf.run()\n\t\t"
             "model.load_weights(weightfile)\n\t"

             "class_names = utils.load_class_names(class_name)\n\t"
             "cap = cv2.VideoCapture(cameraSource["+str(i)+"])\n\t"

             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "timeStamp = []\n\t\t"
             "crowdNum = []\n\t\t"
             "frameIndex = 0\n\t\t"
             "sourceFileName = []\n\t\t"
             "classIndex = [None]*len(run"+str(i)+".class_names)\n\t\t"
             "classesName = []\n\t\t"
             "datetimeFormat = datetime.now().strftime(\"%Y/%m/%d-%H:%M:%S.%f\")[:-3]\n\t\t"
             "videoName=\"\".join(re.split(\"/|:\",datetimeFormat))\n\t\t"
             "videoName=\"\".join((videoName,\".mp4\"))\n\t\t"
             "frame_size = (int(run"+str(i)+".cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(run"+str(i)+".cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))\n\n\t\t"
             "videoWrite = cv2.VideoWriter(os.path.join(processedVideoDir,videoName),cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),frameRate,frame_size)\n\t\t"

             "start1 = time.perf_counter()\n\t\t"
             "detectInfo = []\n\n\t\t"

             "try:\n\t\t\t"
             "while True:\n\t\t\t\t"
             "start = time.time()\n\t\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t\t"
             "if not ret:\n\t\t\t\t\t"
             "break\n\n\t\t\t\t"

             "resized_frame = tf.expand_dims(frame, 0)\n\t\t\t\t"
             "resized_frame = utils.resize_image(resized_frame, (model_size[0], model_size[1]))\n\t\t\t\t"

             "pred = run" +
             str(i)+".model.predict(resized_frame)\n\t\t\t\t"

             "boxes, scores, classes, nums = utils.output_boxes(\n\t\t\t\t\t"
             "pred, model_size,\n\t\t\t\t\t"
             "max_output_size=max_output_size,\n\t\t\t\t\t"
             "max_output_size_per_class=max_output_size_per_class,\n\t\t\t\t\t"
             "iou_threshold=iou_threshold,\n\t\t\t\t\t"
             "confidence_threshold=confidence_threshold)\n\n\t\t\t\t"

             "img, getTime, persons, bboxes = utils.draw_outputs(\n\t\t\t\t\t"
             "frame, boxes, scores, classes, nums, run" +
             str(i)+".class_names)\n\t\t\t\t"
             "cv2.putText(img, datetime.now().strftime(\"%Y/%m/%d-%H:%M:%S.%f\")\n\t\t\t\t\t\t\t"
             "[:-3], (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)\n\t\t\t\t"
             "if getTime != 0:\n\t\t\t\t\t"
             "timeStamp.append(getTime)\n\t\t\t\t\t"
             "crowdNum.append(persons)\n\t\t\t\t\t"
             "sourceFileName.append(videoName.split(\".\")[0])\n\t\t\t\t\t"
             "if classIndex[0] is None:\n\t\t\t\t\t\t"
             "classIndex[0] = [frameIndex]\n\t\t\t\t\t"
             "else:\n\t\t\t\t\t\t"
             "classIndex[0].append(frameIndex)\n\n\t\t\t\t"
             "videoWrite.write(img)\n\n\t\t\t\t"

             "_, img2 = cv2.imencode(\".jpg\", img)\n\t\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t\t"

             "yield img2\n\n\t\t\t\t"

             "stop = time.time()\n\t\t\t\t"

             "seconds = stop - start\n\t\t\t\t"

             "fps = 1 / seconds\n\t\t\t\t"
             "print(\"Estimated frames per second : {0}\".format(fps))\n\t\t\t\t"
             "if frameIndex == 50:\n\t\t\t\t\t"
             "break\n\t\t\t\t"
             "frameIndex += 1\n\t\t\t\t"

             "key = cv2.waitKey(1) & 0xFF\n\t\t\t\t"

             "if key == ord('q'):\n\t\t\t\t\t"
             "break\n\t\t"
             "finally:\n\t\t\t"
             "cv2.destroyAllWindows()\n\t\t\t"
                    "run"+str(i)+".cap.release()\n\t\t\t"
                    "videoWrite.release()\n\t\t\t"
                    "print('Detections have been performed successfully.')\n\t\t"
             "end1 = time.perf_counter()-start1\n\t\t"
             "print(\"finish\", end1)\n\t\t"
             "print(\"Count\", frameIndex)\n\t\t"
             "num_processes = multiprocessing.cpu_count()\n\t\t"
             "print(\"Number of CPU: \" + str(num_processes))\n\t\t"

             "detectInfo = {\"Index\": classIndex,\"crowd\": crowdNum, \"time\": timeStamp, \"Source File\": sourceFileName}\n\t\t"

             "create_CSV.update(detectInfo)\n\t"

             "@staticmethod\n\t"
             "def raw():\n\t\t"
             "while 1:\n\t\t\t"
                    "ret, frame = run"+str(i)+".cap.read()\n\t\t\t"
                    "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t"
                    "yield img1.tobytes()\n\n")


def run():
    for i in range(Streams):
        exec("run"+str(i)+"()")


if __name__ == '__main__':
    run()
