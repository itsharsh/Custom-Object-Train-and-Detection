import tensorflow as tf
from yolov3 import utils
import cv2
import time
import multiprocessing
from datetime import datetime

import path_config
from yolov3 import yolov3
from DB import create_CSV

model_size = (352, 352, 3)
num_classes = 80
class_name = path_config.namePath
max_output_size = 100
max_output_size_per_class = 20
iou_threshold = 0.5
confidence_threshold = 0.5


cfgfile = path_config.configPath
weightfile = path_config.weightPath


class run():

    model = yolov3.YOLOv3Net(cfgfile, model_size, num_classes)

    model.load_weights(weightfile)

    class_names = utils.load_class_names(class_name)

    # specify the vidoe input.
    # 0 means input from cam 0.
    # For vidio, just change the 0 to video path
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(0)
    prop = cv2.CAP_PROP_FRAME_COUNT
    total = int(cap.get(prop))
    frame_size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH),
                  cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    @staticmethod
    def processed():
        count = 0
#        prevCount = 0
        timeStamp = []
        crowdNum = []
        index = 0
        classIndex = []
        classesName = []
        start1 = time.perf_counter()
        detectInfo = []

        try:
            while True:
                start = time.time()
                ret, frame = run.cap.read()
                _, img1 = cv2.imencode(".jpg", frame)
                img1 = img1.tobytes()
                if not ret:
                    break

                resized_frame = tf.expand_dims(frame, 0)
                resized_frame = utils.resize_image(
                    resized_frame, (model_size[0], model_size[1]))

                pred = run.model.predict(resized_frame)

                boxes, scores, classes, nums = utils.output_boxes(
                    pred, model_size,
                    max_output_size=max_output_size,
                    max_output_size_per_class=max_output_size_per_class,
                    iou_threshold=iou_threshold,
                    confidence_threshold=confidence_threshold)

                img, getTime, persons = utils.draw_outputs(
                    frame, boxes, scores, classes, nums, run.class_names)
                cv2.putText(img, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")
                            [:-3], (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
                if getTime != 0:
                    timeStamp.append(getTime)
                    crowdNum.append(persons)
                    index += 1
                    classIndex.append(index)

                _, img2 = cv2.imencode(".jpg", img)
                img2 = img2.tobytes()

                yield img2

                stop = time.time()

                seconds = stop - start
                # print("Time taken : {0} seconds".format(seconds))

                # Calculate frames per second
                fps = 1 / seconds
                print("Estimated frames per second : {0}".format(fps))
                # if count == 100:
                #    break
                count += 1

                key = cv2.waitKey(1) & 0xFF

                if key == ord('q'):
                    break
        finally:
            cv2.destroyAllWindows()
            run.cap.release()
            print('Detections have been performed successfully.')
        end1 = time.perf_counter()-start1
        print("finish", end1)
        print("total frame", total)
        print("Count", count)
        num_processes = multiprocessing.cpu_count()
        print("Number of CPU: " + str(num_processes))

        detectInfo = {"Index": classIndex,
                      "crowd": crowdNum, "time": timeStamp}

        create_CSV.update(detectInfo)

    @staticmethod
    def raw():
        while 1:
            ret, frame = run.cap.read()
            _, img1 = cv2.imencode(".jpg", frame)
            yield img1.tobytes()


def Run():
    run()


if __name__ == '__main__':
    Run()
