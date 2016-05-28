#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "Bu betigin calismasi icin root yetkisi gereklidir." 
   exit 1
fi

apt-get install xsel
apt-get install python-bs4
apt-get install python-gobject
