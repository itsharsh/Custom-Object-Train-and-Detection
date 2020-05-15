import os
import platform

if platform.system() == "Windows":
    if(os.getlogin() == "Harsh"):
        sasDir = os.path.join(
            "D:\\", "Office", "Backup", "Projects Data", "Situational_Awareness_System")

    elif(os.getlogin() == "Ajeet"):
        sasDir = os.path.join(
            "D:\\", "Office", "Backup", "Projects Data", "Situational_Awareness_System")

elif platform.system() == "Linux":
    if(os.getlogin() == "harsh"):
        sasDir = "/home/vivek/Test_Videos/"

    elif(os.getlogin() == "vivek"):
        sasDir = "/home/vivek/Test_Videos/"

cameraSource = [0]

hostname = 'localhost'
port = 8888

dbFilePath = os.path.join(sasDir, "DB", "sas.csv")

modelName = "yolov3ORIG"
modelDir = os.path.join(sasDir, "Model")
tfWeightFile = os.path.join(modelDir, modelName, modelName+".tf")
configFilePath = os.path.join(modelDir, modelName, modelName+".cfg")
namesFilePath = os.path.join(modelDir, modelName, modelName+".names")
weightsFilePath = os.path.join(modelDir, modelName, modelName + ".weights")

originalVideoDir = os.path.join(sasDir, "Original")
processedVideoDir = os.path.join(sasDir, "Processed")
