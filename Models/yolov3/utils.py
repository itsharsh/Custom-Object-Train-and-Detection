"""
Written by: Rahmad Sadli
Website : https://machinelearningspace.com

I finally made this program simple and readable
Hopefully, this program will help some beginners like me to understand better object detection.
If you want to redistribute it, just keep the author's name.

In oder to execute this program, you need to install TensorFlow 2.0 and opencv 4.x

For more details about how this program works. I explained well about it, just click the link below:
https://machinelearningspace.com/the-beginners-guide-to-implementing-yolo-v3-in-tensorflow-2-0-part-1/

Credit to:
Ayoosh Kathuria who shared his great work using pytorch, really appreaciated it.
https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/
"""

import tensorflow as tf
import numpy as np
import cv2
import time
from datetime import datetime

timeStamp = 0


def resize_image(inputs, modelsize):
    inputs = tf.image.resize(inputs, modelsize)
    return inputs


def output_boxes(inputs, model_size, max_output_size, max_output_size_per_class,
                 iou_threshold, confidence_threshold):

    center_x, center_y, width, height, confidence, classes = \
        tf.split(inputs, [1, 1, 1, 1, 1, -1], axis=-1)

    top_left_x = center_x - width / 2.0
    top_left_y = center_y - height / 2.0
    bottom_right_x = center_x + width / 2.0
    bottom_right_y = center_y + height / 2.0

    inputs = tf.concat([top_left_x, top_left_y, bottom_right_x,
                        bottom_right_y, confidence, classes], axis=-1)

    boxes_dicts = non_max_suppression(inputs, model_size, max_output_size,
                                      max_output_size_per_class, iou_threshold, confidence_threshold)

    return boxes_dicts


def draw_outputs(img, boxes, objectness, classes, nums, class_names):
    # def draw_outputs(img, boxes, objectness, classes, nums, class_names,prevCount):
    boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
    boxes = np.array(boxes)
    count = 0
    timeStamp = 0
    bboxes=[]
    for i in range(nums):
        if class_names[int(classes[i])] == 'person':

            box = (tuple(
                (boxes[i, 0:2] * [img.shape[1], img.shape[0]]).astype(np.int32)),
                tuple(
                (boxes[i, 2:4] * [img.shape[1], img.shape[0]]).astype(np.int32)))
            timeStamp = datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3]

            img = cv2.rectangle(img, box[0], box[1], (255, 0, 0), 2)
            count += 1
            bboxes.append(box)
    print("crowd:",count)
    return img, timeStamp, count,bboxes


def load_class_names(file_name):
    with open(file_name, 'r') as f:
        class_names = f.read().splitlines()
    return class_names


def non_max_suppression(inputs, model_size, max_output_size,
                        max_output_size_per_class, iou_threshold, confidence_threshold):
    bbox, confs, class_probs = tf.split(inputs, [4, 1, -1], axis=-1)
    bbox = bbox/model_size[0]

    scores = confs * class_probs
    boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
        boxes=tf.reshape(bbox, (tf.shape(bbox)[0], -1, 1, 4)),
        scores=tf.reshape(
            scores, (tf.shape(scores)[0], -1, tf.shape(scores)[-1])),
        max_output_size_per_class=max_output_size_per_class,
        max_total_size=max_output_size,
        iou_threshold=iou_threshold,
        score_threshold=confidence_threshold
    )
    return boxes, scores, classes, valid_detections
