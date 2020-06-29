import os
import csv
import sys
import platform
import pandas as pd
from datetime import timedelta

import path_config

dbFilePath = path_config.dbFilePath


def getStartEnd(nums):
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))


def updateDBIndex():
    try:
        df = pd.read_csv(dbFilePath)
        return df["DB Index"].max()+1  # add 1 for counter

    except pd.errors.EmptyDataError:
        print("Empty CSV File")
        return 1


def updateCSV(row):
    with open(dbFilePath, mode='a+', newline='') as csvFile:
        fileWriter = csv.writer(csvFile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fileWriter.writerow(row)


def update(detectInfo):
    try:
        for i, classList in enumerate(detectInfo["Index"]):
            if classList is not None:
                # classList = getStartEnd(classList)
                for j in range(len(classList)):
                    index = updateDBIndex()
                    crowds = detectInfo["crowd"][j]
                    date = detectInfo["time"][j].split("-")[0]
                    time = detectInfo["time"][j].split("-")[1]
                    sourceFileName = detectInfo["Source File"][j]

                    header = ["DB Index", "Date", "Time", "Total Persons Count", "Source File"]

                    row = [index, date, time, crowds, sourceFileName]

                    if index == 1:
                        updateCSV(header)
                    updateCSV(row)
        print("DB Updated")
    except FileNotFoundError:
        csvCreate = open(dbFilePath, mode='w', newline='')
        update(detectInfo)
    except:
        print("Exception while updating DB: ", sys.exc_info())