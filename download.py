# coding=utf-8

import xml.dom.minidom
from xml.dom.minidom import parse
import os
import subprocess
import sys
import time

__DEFAULT_DOWNLOADER__ = "/usr/bin/wget"
__DEFAULT_OUTPUT_PATH__ = "output"
__DEFAULT_ERRLOG__ = "error.log"


class DownloadTask:
    def __init__(self, TaskName = "", TaskUrl = ""):
        self.TaskName = TaskName
        self.TaskUrl = TaskUrl



# Load XML file "list.xml"
DOMTree = xml.dom.minidom.parse("list.xml")
DOMDownList = DOMTree.documentElement
DOMTasks = DOMDownList.getElementsByTagName("task")

# Download data
DownloadList = []

# Parse XML file 
for task in DOMTasks:
    if task.getElementsByTagName('isDownload')[0].childNodes[0].data == "true":
        print("Task: {}".format(task.getAttribute("title")))
        print("  Url: {}".format(task.getElementsByTagName('url')[0].childNodes[0].data))
        DownloadList.append(DownloadTask(task.getAttribute("title"), task.getElementsByTagName('url')[0].childNodes[0].data))
    else:
        pass

# How to download 
def Download(url, Downloader, OutputPath, AppendArgs = " "):
    return os.system("/usr/bin/wget -P {}  {}".format(OutputPath, url) + os.devnull)
    #return subprocess.run([Downloader, "-P ".format(OutputPath), AppendArgs, url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode

# Write error log
def Errlog(url, ErrLogPath):
    ErrLogFile = open(ErrLogPath, mode="w+")
    ErrLogFile.write("[Failed] time=\"{}\", url=\"{}\"".format(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), url))
    ErrLogFile.close()

# Start Download
if len(DownloadList) == 0:
    print("No Tasks.")
    sys.exit(0)
else:
    for task in DownloadList:
        os.system("mkdir -p output")
        os.system("output/{}".format(task.TaskName))
        if Download(task.TaskUrl, __DEFAULT_DOWNLOADER__, __DEFAULT_OUTPUT_PATH__ + "/"+ task.TaskName) == 0:
            print("  Finish downloading from {}".format(task.TaskUrl))
        else:
            print("Cannot download from {}".format(task.TaskUrl))
            # Clean Log
            #os.remove(__DEFAULT_OUTPUT_PATH__)
            #os.remove(__DEFAULT_ERRLOG__)
            Errlog(task.TaskUrl, __DEFAULT_ERRLOG__)
    print("Finish all")

# Print error log to tty
with open(__DEFAULT_ERRLOG__, 'r') as file:
    for line in file:
        print(line)