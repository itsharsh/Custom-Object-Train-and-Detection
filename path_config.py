import os
import platform

if platform.system() == "Windows":
    sasDir = os.path.join(
        "D:\\", "Office", "Backup", "Projects Data", "AI", "Situational_Awareness_System", "Test Videos")
    gitRepoDir = os.path.join(
        "D:\\", "Office", "Google Drive", "Projects", "AI", "Situational Awareness System", "SAS")

elif platform.system() == "Linux":
    sasDir = "/home/vivek/Test_Videos/"
    gitRepoDir = os.path.join("~/", "Test_Videos")

cameraSource = [0, "videoplayback (1).mp4","videoplayback (2).mp4","videoplayback (3).mp4","videoplayback (4).mp4","videoplayback (5).mp4"]#, "video2.mp4", "video2clip1.mp4", "weapontest.mp4", "weapontest2.mp4",
                #"weapontest3.mp4", "weapontest4.mp4"]
