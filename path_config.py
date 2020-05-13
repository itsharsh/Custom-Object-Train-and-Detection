import os
import platform

if platform.system() == "Windows":
    sasDir = os.path.join(
        "D:\\", "Office", "Backup", "Projects Data", "AI", "Situational_Awareness_System")

    gitRepoDir = os.path.join(
        "D:\\", "Office", "Google Drive", "Projects", "AI", "Situational Awareness System", "SAS")

elif platform.system() == "Linux":
    detectPer = "/home/vivek/SAS/Detectperson/"
    sasDir = "/home/vivek/Test_Videos/"
    gitRepoDir = os.path.join("~/", "Test_Videos")

# cameraSource = [0, "video1.mp4", "video2.mp4", "video2clip1.mp4", "weapontest.mp4", "weapontest2.mp4",
 #               "weapontest3.mp4", "weapontest4.mp4"]
cameraSource = [0, 1]

detectPer = os.path.join(sasDir, "Detectperson")


#dbDir = os.path.join(gitRepoDir, "DB")
dbDir = os.path.join(sasDir, "DB")
dbFilePath = os.path.join(dbDir, "adtrack.csv")

modelDir = os.path.join(sasDir, "Model")
originalVideoDir = os.path.join(sasDir, "Original Videos")
processedVideoDir = os.path.join(sasDir,  "Processed Videos")

weightPath = os.path.join(detectPer, "Models", "yolov3_weights.tf")
configPath = os.path.join(detectPer, "Models", "yolov3.cfg")
namePath = os.path.join(detectPer, "Models", "coco.names")
csvPath = os.path.join(detectPer, "CSV", "crowd.csv")
#testVideo = os.path.join("/home/vivek/", "Test_Videos")
#testVideo = os.path.join(testVideo, "videoplayback (2).mp4")

# videoPath = 0  # webcam
