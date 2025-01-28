#!/bin/bash

source envsetup.sh

${PYTHON} download.py

/usr/bin/bash makezip.sh