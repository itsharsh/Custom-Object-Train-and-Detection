from __future__ import print_function
import sys
import cv2
from random import randint
import time
import path_config
cameraSource = path_config.cameraSource
videoPath = path_config.originalVideoDir


def trackingFrame(frame,bboxes,colors):
    while True:
        # draw bounding boxes over objects
        # selectROI's default behaviour is to draw box starting from the center
        # when fromCenter is set to false, you can draw box starting from top left corner
        bbox = cv2.selectROI('Frame', frame)
        bboxes.append(bbox)
        colors.append((randint(64, 255), randint(64, 255), randint(64, 255)))
        print("Press q to quit selecting boxes and start tracking")
        print("Press any other key to select next object")
        k = cv2.waitKey(0) & 0xFF
        if (k == 113):  # q is pressed
            break
            
    print('Selected bounding boxes {}'.format(bboxes))

    multiTracker = cv2.MultiTracker_create()

    for bbox in bboxes:
        multiTracker.add(cv2.TrackerCSRT_create(), frame, bbox)
    return bboxes,colors,multiTracker




def run():
    prevbox=[]
    print("Default tracking algoritm is CSRT \n"
            "Available tracking algorithms are:\n")      

    cap = cv2.VideoCapture(videoPath+cameraSource[1])
    (W, H) = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    while True:
        
        # Read first frame
        success, frame = cap.read()
        # quit if unable to read the video file
        if not success:
            print('Failed to read video')
            sys.exit(1)


        ## Select boxes
        bboxes = []
        colors = []

        if cv2.waitKey(1) & 0xFF == 32:
        # OpenCV's selectROI function doesn't work for selecting multiple objects in Python
        # So we will call this function in a loop till we are done selecting all objects
            bboxes,colors,multiTracker=trackingFrame(frame,bboxes,colors)
        if bboxes!=[]:
            break
        time.sleep(0.04)
        cv2.imshow("Frame",frame)
    # Process video and track objects
    if bboxes!=[]:
        while cap.isOpened():
            t1=time.time()
            success, frame = cap.read()
            if not success:
                break
            
            # get updated location of objects in subsequent frames
            success, boxes = multiTracker.update(frame)

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
                cv2.rectangle(frame, p1, p2, colors[i], 2, 1)
                time.sleep(0.04)
                prevbox=newbox
                # yield boxes,(W,H)
                cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == 32:
                bboxes,colors=[],[]
                bboxes,colors,multiTracker=trackingFrame(frame,bboxes,colors,trackerType)
            if cv2.waitKey(1) & 0xFF == 119:# w to remove all boxes
                bboxes,colors=[] , []

            end=time.time()-t1
            fps=1/end
            # print("Fps",fps)
            

            # quit on ESC button
            if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
                break






if __name__ == '__main__':
    run()