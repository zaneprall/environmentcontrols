#!/bin/bash


wget -q --spider http://google.com

if [ $? -eq 0 ]; then
    echo "Still working. "
else    echo "Something broke. restarting stuff. "
sudo systemctl restart networking
fi

#script used as an easy fix for a rasberry pi zero w eventually losing networking. set via cron
