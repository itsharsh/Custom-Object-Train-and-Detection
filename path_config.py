import os
import platform

if platform.system() == "Windows":
    testVideos = "D://Office//Google Drive//Projects//AI//Situational Awareness System//O2i-SAS//"

elif platform.system() == "Linux":
    adTrackerDir = "/home/vivek/Test_Videos/"
    gitRepoDir = os.path.join("~/", "Test_Videos")

cameraSource = [0, "test2.mp4", "test3.mp4", "test4.mp4", "test5.mp4", "test6.mp4",
                "test7.mp4", "test8.mp4", "test9.mp4", "test10.mp4", "test11.mp4", "test12.mp4"]
