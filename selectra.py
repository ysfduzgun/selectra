#/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8
# Yusuf Duzgun yzduzgun@gmail.com
# License : GPL3

import os
from bs4 import BeautifulSoup
import urllib3
import subprocess

def searchTureng(word):
    http=urllib3.PoolManager()
    url="http://www.tureng.com/search/"+word
    try:
        answer = http.request('GET', url)
    except:
        return "No connection"
    soup = BeautifulSoup(answer.data)
    trlated=''
    try:
        table = soup.find('table')
        td = table.findAll('td', attrs={'lang':'tr'})
        for val in td[0:5]:
            trlated = trlated + val.text + '\n'
        return trlated
    except:
        return "Not Found !"

selectedText = os.popen('xsel').read()
#print (selectedText)
result = searchTureng(selectedText)
#print (result)
subprocess.Popen(["notify-send", selectedText, result])
