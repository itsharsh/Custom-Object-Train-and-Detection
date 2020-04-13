import os
import platform

if platform.system() == "Windows":
    adTrackerDir = "D:/Test/"
    gitRepoDir = os.path.join(
        "D:/Office/Google Drive/Projects/AI/AdTracker", "O2i-Adtracker")
elif platform.system() == "Linux":
    testVideos = "/home/vivek/Test_Videos/"
    gitRepoDir = os.path.join("~/", "Test_Videos")
    cameraSource = [0,"test2.mp4","test3.mp4","test4.mp4","test5.mp4","test6.mp4","test7.mp4","test8.mp4","test9.mp4","test10.mp4","test11.mp4","test12.mp4"]