#!/usr/bin/env python3.7
import fileinput
from datetime import timedelta, datetime
import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fIn", type=str,
                    help="Path of the input file.")
parser.add_argument("fOut", type=str,
                    help="Path of the output file.")
parser.add_argument("-d", "--delay", type=int, default=1,
                    help="Multiply the delay between each log line by given factor. If 0 there is no delay.")
parser.add_argument("-o", "--offset", type=int, default=0,
                    help="The offset in seconds before the log simulation starts to write to file.")
args = parser.parse_args()

previousDt = 0

def createFile(path):
    try:
        os.remove(path)
    except:
        print("File for writing logs on path " + path +
              " not found, a new file will be created")
    finally:
        print("Created file on path " + path)
        return open(path, "a")

def readFromFileAndWriteToOutPut(pathFOut, pathFIn, delay, offset):
    fOut = createFile(pathFOut)
    time.sleep(offset)
    with fileinput.input(files=pathFIn) as f:
        for line in f:
            currentDt = datetime.fromisoformat(line[1:24])
            if f.isfirstline():
                previousDt = currentDt
            tDelta = currentDt - previousDt
            previousDt = currentDt
            time.sleep(tDelta.total_seconds()*delay)
            print("Appending line to output file " +
                  pathFOut + " : " + line, end='')
            print(line, end='', file=fOut, flush=True)
        print("", file=fOut)


print('{:*^30}'.format('Start log simulator'))
readFromFileAndWriteToOutPut(args.fOut, args.fIn, args.delay, args.offset)
print('{:*^30}'.format('Exit log simulator'))
