import os
import csv
import sys
import platform
import pandas as pd
from datetime import timedelta

import path_config

dbFilePath = path_config.dbFilePath


def update(detectInfo):
    csvCreate = open(dbFilePath, mode='w', newline='')
    with open(dbFilePath, mode='a+', newline='') as csvFile:
        fileWriter = csv.writer(csvFile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ["DB Index", "Date", "Time", "Total Persons Count"]
        # header = ["DB Index", "Date", "Time", "Total Persons Count"]
        fileWriter.writerow(header)
        for i in range(len(detectInfo["Index"])):
            index = detectInfo["Index"][i]
            # classes=detectInfo["class"][i]
            crowds = detectInfo["crowd"][i]
            date = detectInfo["time"][i].split("-")[0]
            time = detectInfo["time"][i].split("-")[1]
            row = [index, date, time, crowds]
            fileWriter.writerow(row)
    print("Csv Created")
