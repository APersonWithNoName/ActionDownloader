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

# Install python moudles