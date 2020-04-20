import os
import platform

if platform.system() == "Windows":
    testVideos = "D://Office//Google Drive//Projects//AI//Situational Awareness System//O2i-SAS//"

elif platform.system() == "Linux":
    testVideos = "/home/vivek/Test_Videos/"
    gitRepoDir = os.path.join("~/", "Test_Videos")

cameraSource = [0, "1.mp4", "2.mp4", "3.mp4", "4.mp4", "5.mp4"]
