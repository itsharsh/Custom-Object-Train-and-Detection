import os
import getpass
import platform

if platform.system() == "Windows":
    if(os.getlogin() == "Harsh"):
        sasDir = os.path.join(
            "D:\\", "Office", "Backup", "Projects Data", "SAS")

    elif(os.getlogin() == "Ajeet"):
        sasDir = os.path.join(
            "D:\\", "Office", "Backup", "Projects Data", "SAS")

elif platform.system() == "Linux":
    if(getpass.getuser() == "ai-ctrl"):
        sasDir = os.path.join(
            "/home", "ai-ctrl", "Aj___", "Office", "Backup", "Projects_Data", "AI", "Situational_Awareness_System")

    elif(os.getlogin() == "harsh"):
        sasDir = os.path.join(
            "/home", "harsh", "media", "Projects Data","SAS")

    elif(os.getlogin() == "vivek"):
        sasDir = os.path.join(
            "/home","vivek","Projects Data","SAS")

cameraSource = [0,"1"]

hostname = 'localhost'
port = 8888

dbFilePath = os.path.join(sasDir, "DB", "sas.csv")

#modelName = "yolov3ORIG"
#modelName="LicencePlate"
modelName = "LPdetect"
modelDir = os.path.join(sasDir, "Model")
tfWeightFile = os.path.join(modelDir, modelName, modelName+".tf")
configFilePath = os.path.join(modelDir, modelName, modelName+".cfg")
namesFilePath = os.path.join(modelDir, modelName, modelName+".names")
weightsFilePath = os.path.join(modelDir, modelName, modelName + ".weights")

originalVideoDir = os.path.join(sasDir, "Original")
processedVideoDir = os.path.join(sasDir, "Processed")
