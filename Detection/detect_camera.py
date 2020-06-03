import cv2
import time
import tensorflow as tf
from datetime import datetime

import path_config
from DB import create_CSV
from Models.yolov3 import utils
from Models.yolov3 import yolov3
from Models import convert_weights_tf

model_size = (352, 352, 3)
num_classes = 80
max_output_size = 100
max_output_size_per_class = 20
iou_threshold = 0.5
confidence_threshold = 0.5


cfgfile = path_config.configFilePath
class_name = path_config.namesFilePath
weightfile = path_config.tfWeightFile

cameraSource = path_config.cameraSource
videoPath = path_config.originalVideoDir

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

             "cap = cv2.VideoCapture(videoPath+cameraSource["+str(i)+"])\n\t"
             "prop = cv2.CAP_PROP_FRAME_COUNT\n\t"
             "total = int(cap.get(prop))\n\t"
             "frame_size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))\n\n\t"

             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "count = 0\n\t\t"
             "timeStamp = []\n\t\t"
             "crowdNum = []\n\t\t"
             "index = 0\n\t\t"
             "classIndex = []\n\t\t"
             "classesName = []\n\t\t"
             "start1 = time.perf_counter()\n\t\t"
             "detectInfo = []\n\n\t\t"

             "try:\n\t\t\t"
             "while True:\n\t\t\t\t"
             "start = time.time()\n\t\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t\t"
             "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t\t"
             "img1 = img1.tobytes()\n\t\t\t\t"
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

             "img, getTime, persons = utils.draw_outputs(\n\t\t\t\t\t"
             "frame, boxes, scores, classes, nums, run" +
             str(i)+".class_names)\n\t\t\t\t"
             "cv2.putText(img, datetime.now().strftime(\"%Y/%m/%d-%H:%M:%S.%f\")\n\t\t\t\t\t\t\t"
             "[:-3], (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)\n\t\t\t\t"
             "if getTime != 0:\n\t\t\t\t\t"
             "timeStamp.append(getTime)\n\t\t\t\t\t"
             "crowdNum.append(persons)\n\t\t\t\t\t"
             "index += 1\n\t\t\t\t\t"
             "classIndex.append(index)\n\n\t\t\t\t"

             "_, img2 = cv2.imencode(\".jpg\", img)\n\t\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t\t"

             "yield img2\n\n\t\t\t\t"

             "stop = time.time()\n\t\t\t\t"

             "seconds = stop - start\n\t\t\t\t"

             "fps = 1 / seconds\n\t\t\t\t"
             "print(\"Estimated frames per second : {0}\".format(fps))\n\t\t\t\t"
             # if count == 100:
             #    break
             "count += 1\n\t\t\t\t"

             "key = cv2.waitKey(1) & 0xFF\n\t\t\t\t"

             "if key == ord('q'):\n\t\t\t\t\t"
             "break\n\t\t"
             "finally:\n\t\t\t"
             "cv2.destroyAllWindows()\n\t\t\t"
                    "run"+str(i)+".cap.release()\n\t\t\t"
                    "print('Detections have been performed successfully.')\n\t\t"
             "end1 = time.perf_counter()-start1\n\t\t"
             "print(\"finish\", end1)\n\t\t"
             "print(\"total frame\", total)\n\t\t"
             "print(\"Count\", count)\n\t\t"
             "print(\"Number of CPU: \" + str(num_processes))\n\t\t"

             "detectInfo = {\"Index\": classIndex,\"crowd\": crowdNum, \"time\": timeStamp}\n\t\t"

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
             "prop = cv2.CAP_PROP_FRAME_COUNT\n\t"
             "total = int(cap.get(prop))\n\t"
             "frame_size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))\n\n\t"

             "@staticmethod\n\t"
             "def processed():\n\t\t"
             "count = 0\n\t\t"
             "timeStamp = []\n\t\t"
             "crowdNum = []\n\t\t"
             "index = 0\n\t\t"
             "classIndex = []\n\t\t"
             "classesName = []\n\t\t"
             "start1 = time.perf_counter()\n\t\t"
             "detectInfo = []\n\n\t\t"

             "try:\n\t\t\t"
             "while True:\n\t\t\t\t"
             "start = time.time()\n\t\t\t\t"
             "ret, frame = run"+str(i)+".cap.read()\n\t\t\t\t"
             "_, img1 = cv2.imencode(\".jpg\", frame)\n\t\t\t\t"
             "img1 = img1.tobytes()\n\t\t\t\t"
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

             "img, getTime, persons = utils.draw_outputs(\n\t\t\t\t\t"
             "frame, boxes, scores, classes, nums, run" +
             str(i)+".class_names)\n\t\t\t\t"
             "cv2.putText(img, datetime.now().strftime(\"%Y/%m/%d-%H:%M:%S.%f\")\n\t\t\t\t\t\t\t"
             "[:-3], (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)\n\t\t\t\t"
             "if getTime != 0:\n\t\t\t\t\t"
             "timeStamp.append(getTime)\n\t\t\t\t\t"
             "crowdNum.append(persons)\n\t\t\t\t\t"
             "index += 1\n\t\t\t\t\t"
             "classIndex.append(index)\n\n\t\t\t\t"

             "_, img2 = cv2.imencode(\".jpg\", img)\n\t\t\t\t"
             "img2 = img2.tobytes()\n\n\t\t\t\t"

             "yield img2\n\n\t\t\t\t"

             "stop = time.time()\n\t\t\t\t"

             "seconds = stop - start\n\t\t\t\t"

             "fps = 1 / seconds\n\t\t\t\t"
             "print(\"Estimated frames per second : {0}\".format(fps))\n\t\t\t\t"
             # if count == 100:
             #    break
             "count += 1\n\t\t\t\t"

             "key = cv2.waitKey(1) & 0xFF\n\t\t\t\t"

             "if key == ord('q'):\n\t\t\t\t\t"
             "break\n\t\t"
             "finally:\n\t\t\t"
             "cv2.destroyAllWindows()\n\t\t\t"
                    "run"+str(i)+".cap.release()\n\t\t\t"
                    "print('Detections have been performed successfully.')\n\t\t"
             "end1 = time.perf_counter()-start1\n\t\t"
             "print(\"finish\", end1)\n\t\t"
             "print(\"total frame\", total)\n\t\t"
             "print(\"Count\", count)\n\t\t"
             "print(\"Number of CPU: \" + str(num_processes))\n\t\t"

             "detectInfo = {\"Index\": classIndex,\"crowd\": crowdNum, \"time\": timeStamp}\n\t\t"

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
