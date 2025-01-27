#!/usr/bin/env python3
# coding=utf-8

import xml.dom.minidom
from xml.dom.minidom import parse
import os
import subprocess
import sys
import time

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
        DownloadList.append(task.getElementsByTagName('url')[0].childNodes[0].data)
    else:
        pass

# How to download 
DefaultDownloader = "/usr/bin/wget"
DefaultOutPath = "."
AppendArgs = "-P {}".format(DefaultOutPath)
def Download(url):
    return subprocess.run([DefaultDownloader, AppendArgs, url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode

# Write error log
DefaultErrLog = "ERRORS.log"
def Errlog(url):
    ErrLogFile = open(DefaultErrLog, mode="w+")
    ErrLogFile.write("[Failed] time=\"{}\", url=\"{}\"".format(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), url))
    ErrLogFile.close()

# Start Download
if len(DownloadList) == 0:
    print("No Tasks.")
    sys.exit(0)
else:
    for url in DownloadList:
        if Download(url) == 0:
            print("  Finish downloading from {}".format(url))
        else:
            print("Cannot download from {}".format(url))
            # Clean Log
            os.remove(DefaultErrLog)
            Errlog(url)
    print("Finish all")

# Print error log to tty
with open(DefaultErrLog, 'r') as file:
    for line in file:
        print(line)