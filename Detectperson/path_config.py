import os
import platform

if platform.system() == "Windows":
    detectPer = os.path.join(
        "D:\\", "Office", "Backup", "Projects Data", "AI", "Situational_Awareness_System", "Test Videos")
    gitRepoDir = os.path.join(
        "D:\\", "Office", "Google Drive", "Projects", "AI", "Situational Awareness System", "SAS")

elif platform.system() == "Linux":
    detectPer = "/home/vivek/SAS/Detectperson/"
    gitRepoDir = os.path.join("~/", "SAS/Detectperson/")

weightPath=os.path.join(detectPer,"Models","yolov3_weights.tf")
configPath=os.path.join(detectPer,"Models","yolov3.cfg")
namePath=os.path.join(detectPer,"Models","coco.names")
csvPath=os.path.join(detectPer,"CSV","crowd.csv")
testVideo=os.path.join("/home/vivek/","Test_Videos")
testVideo=os.path.join(testVideo,"videoplayback (2).mp4")

videoPath=0 # webcam
