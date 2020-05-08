import os
import csv
import sys
import platform
import pandas as pd
from datetime import timedelta


dbFilePath = "/home/vivek/myCsv.csv"


def update(detectInfo):
    csvCreate = open(dbFilePath, mode='w', newline='')
    print("Done")
    with open(dbFilePath, mode='a+', newline='') as csvFile:
        fileWriter = csv.writer(csvFile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print("Done")
        header=["Index","Date","Time","Total Persons Count"]
        fileWriter.writerow(header) 
        for i in range(len(detectInfo["Index"])):
            index=detectInfo["Index"][i]
            # classes=detectInfo["class"][i]
            crowds=detectInfo["crowd"][i]
            date=detectInfo["time"][i].split("-")[0]
            time=detectInfo["time"][i].split("-")[1]
            row=[index,date,time,crowds]  
            fileWriter.writerow(row)
        print("Done")