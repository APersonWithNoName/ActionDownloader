#!/bin/bash

# Check python
if [ -e /usr/bin/python3.11 ];
then
    export PYTHON=/usr/bin/python3.11
elif [ -e /usr/bin/python3 ];
then
    export PYTHON=/usr/bin/python3
elif [ -e /usr/bin/python ];
then
    export PYTHON=/usr/bin/python
else
    echo -e "\033[31mNO PYTHON FOUND!\033[0m"
    exit 1
fi

# Check wget
if [ -e /usr/bin/wget ] && [ -e /bin/wget ];
then
    echo ""
else
    exit 1
fi

# Create virtual environment
${PYTHON} -m venv venv
export VENV_PYTHON=venv/bin/python
export VENV_PIP=venv/bin/pip

if [ $? -ne 0 ];then
    exit 1
fi
# Install python moudles
${VENV_PIP} install -r requirements.txt

if [ $? -ne 0 ];
then
    exit 1
fi
