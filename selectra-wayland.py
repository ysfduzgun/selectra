#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8
# Yusuf Duzgun yzduzgun@gmail.com
# License : GPL3

import os, sys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import subprocess

def searchTureng(word):
    url="http://www.tureng.com/search/"+word
    data = ""
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read()
    except:
        return "No connection"
    soup = BeautifulSoup(data, 'html.parser')
    trlated=''
    try:
        table = soup.find('table')
        td = table.findAll('td', attrs={'lang':'tr'})
        for val in td[0:5]:
            trlated = trlated + val.text + '\n'
        return trlated
    except:
        return "Not Found !"

if len(sys.argv) > 1:
    selectedText = sys.argv[1]
else:
    selectedText = os.popen('wl-paste -p').read()

result = searchTureng(selectedText)
subprocess.Popen(["notify-send", selectedText, result])
