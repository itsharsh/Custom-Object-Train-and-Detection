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

# cameraSource = [0, "video1.mp4", "video2.mp4", "video2clip1.mp4", "weapontest.mp4", "weapontest2.mp4",
 #               "weapontest3.mp4", "weapontest4.mp4"]
cameraSource = [0]

#dbDir = os.path.join(gitRepoDir, "DB")
dbDir = os.path.join(sasDir, "DB")
dbFilePath = os.path.join(dbDir, "adtrack.csv")

modelDir = os.path.join(sasDir, "Model")
originalVideoDir = os.path.join(sasDir, "Original Videos")
processedVideoDir = os.path.join(sasDir,  "Processed Videos")
#recordingVideoDir = os.path.join(sasDir, "Recordings")
#clipsDir = os.path.join(adTrackerDir, "DTH", "Ad Clips")

detectionModelName = "49_Ads"
detectionModelConfigPath = os.path.join(
    modelDir, detectionModelName, detectionModelName + "_test.cfg")
detectionModelClassesPath = os.path.join(
    modelDir, detectionModelName, detectionModelName + ".names")
detectionModelWeightsPath = os.path.join(
    modelDir, detectionModelName, detectionModelName + "_last.weights")

#detectionDate = "20200117"
#detectionChannel = ["Star Sports 1", "Star Sports 1 Hindi"]
#detectionChannel = ["testvid"]
#detectionAd = []
#brandName = "Merinolam"

#brandDir = os.path.join(adTrackerDir, "Brand Data", brandName)

#detectionFilePath = os.path.join(brandDir, brandName+"_FCT.mp4")
#brandNonFCTFilePath = os.path.join(brandDir, "Cropped")
