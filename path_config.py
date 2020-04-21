import os
import platform

if platform.system() == "Windows":
    sasDir = os.path.join(
        "D:\\", "Office", "Backup", "Projects Data", "AI", "Situational_Awareness_System", "Output Videos")
    gitRepoDir = os.path.join(
        "D:\\", "Office", "Google Drive", "Projects", "AI", "Situational Awareness System", "SAS")

elif platform.system() == "Linux":
    sasDir = "/home/vivek/Test_Videos/"
    gitRepoDir = os.path.join("~/", "Test_Videos")

cameraSource = [0, "w1.mp4", "w2clip1.mp4"]
