import os
import platform

if platform.system() == "Windows":
    if(os.getlogin() == "Harsh"):
        sasDir = os.path.join(
            "D:\\", "Office", "Backup", "Projects Data", "SAS")

    elif(os.getlogin() == "Ajeet"):
        sasDir = os.path.join(
            "D:\\", "Office", "Backup", "Projects Data", "SAS")

elif platform.system() == "Linux":
    if(os.getlogin() == "harsh"):
        sasDir = os.path.join(
            "/home", "harsh", "media", "Projects Data","SAS")

    elif(os.getlogin() == "vivek"):
        sasDir = os.path.join(
            "/home","vivek","Projects Data","SAS")

cameraSource = [0,"videoplayback (4).mp4"]

hostname = 'localhost'
port = 8888

dbFilePath = os.path.join(sasDir, "DB", "sas.csv")

modelName = "yolov3ORIG"
modelDir = os.path.join(sasDir, "Model")
tfWeightFile = os.path.join(modelDir, modelName, modelName+".tf")
configFilePath = os.path.join(modelDir, modelName, modelName+".cfg")
namesFilePath = os.path.join(modelDir, modelName, modelName+".names")
weightsFilePath = os.path.join(modelDir, modelName, modelName + ".weights")

originalVideoDir = os.path.join(sasDir, "Original Videos")
processedVideoDir = os.path.join(sasDir, "Processed Videos")
