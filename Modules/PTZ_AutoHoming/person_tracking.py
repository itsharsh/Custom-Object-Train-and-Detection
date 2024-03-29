import cv2
import time
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


cfgfile = path_config.configFilePath
class_name = path_config.namesFilePath
weightfile = path_config.tfWeightFile

cameraSource = path_config.cameraSource
videoPath = path_config.originalVideoDir
circles = []

def mouse_drawing(event, x, y, flags, params):
    global circles
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click")
        circles=(x, y)
        print(circles)


def run():
    global circles
    count=0
    timeStamp=[]
    crowdNum=[]
    index=0
    bbox=0
    classIndex=[]
    classesName=[]
    start1=time.perf_counter()
    detectInfo=[]
    prevbox=[]
    model = yolov3.YOLOv3Net(cfgfile,model_size,num_classes)

    model.load_weights(weightfile)

    class_names = utils.load_class_names(class_name)



    win_name = 'Yolov3 detection'
    cv2.namedWindow(win_name)
    cap = cv2.VideoCapture(videoPath+cameraSource[1])
    prop=cv2.CAP_PROP_FRAME_COUNT
    total=int(cap.get(prop))
    frame_size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH),
                  cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.setMouseCallback(win_name, mouse_drawing)
    print(frame_size)



    try:
        while True:
            start = time.time()
            ret, frame = cap.read()
            if not ret:
                break

            resized_frame = tf.expand_dims(frame, 0)
            resized_frame = utils.resize_image(resized_frame, (model_size[0],model_size[1]))

            pred = model.predict(resized_frame)


            boxes, scores, classes, nums = utils.output_boxes( \
                pred, model_size,
                max_output_size=max_output_size,
                max_output_size_per_class=max_output_size_per_class,
                iou_threshold=iou_threshold,
                confidence_threshold=confidence_threshold)

            img,getTime,persons,bboxes= utils.draw_outputs(frame, boxes, scores, classes, nums, class_names)
            # cv2.putText(img, datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3], (10, 30),cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
            if getTime!=0:
                timeStamp.append(getTime)
                crowdNum.append(persons)
                index+=1
                classIndex.append(index)
            if circles!=[]:
                for box in bboxes:
                    if circles!=[]:
                        if int(box[0][0])<int(circles[0]) and int(box[1][0])>int(circles[0]) and int(box[0][1])<int(circles[1]) and int(box[1][1])>int(circles[1]):
                            print("Perfect")
                            # bbox=(box[0][0],box[0][1],box[1][0],box[1][1])
                            bbox=(box[0][0],box[0][1],box[1][0]-box[0][0],box[1][1]-box[0][1])
                if bbox!=[]:
                    multiTracker = cv2.MultiTracker_create()
                    tracker = cv2.TrackerCSRT_create()
                    print(bbox)
                    multiTracker.add(tracker, img, bbox)
                    while True:
                        success, img = cap.read()
                        success, boxes = multiTracker.update(img)
                        # draw tracked objects
                        for i, newbox in enumerate(boxes):
                            p1 = (int(newbox[0]), int(newbox[1]))
                            p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
                            if prevbox!=[]:
                                if prevbox[0]>p1[0] and (prevbox[0]+prevbox[2])>p2[0]:
                                    print("Pan-Left")
                                elif prevbox[1]>p1[1] and (prevbox[1]+prevbox[3])>p2[1]:
                                    print("Tilt-Down") 
                                elif prevbox[0]<p1[0] and (prevbox[0]+prevbox[2])<p2[0]:
                                    print("Pan-Right")
                                elif prevbox[1]<p1[1] and (prevbox[1]+prevbox[3])<p2[1]:
                                    print("Tilt-Up")
                            prevbox=newbox
                            cv2.rectangle(img, p1, p2, (255,255,0), 2, 1)

                        # show frame
                        time.sleep(0.04)
                        cv2.imshow(win_name, img)
                        

                        # quit on ESC button
                        if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
                            break

            cv2.imshow(win_name, img)
            stop = time.time()

            seconds = stop - start
            fps = 1 / seconds
            print("Estimated frames per second : {0}".format(fps))
            # if count==100:
            #     break
            count+=1

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
    finally:
        cv2.destroyAllWindows()
        cap.release()
        print('Detections have been performed successfully.')

    detectInfo = {"Index":classIndex,"crowd":crowdNum,"time":timeStamp}

    create_CSV.update(detectInfo)



if __name__ == '__main__':
    run()
