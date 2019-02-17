#/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8
# Yusuf Duzgun yzduzgun@gmail.com
# License : GPL3

import os
from gi.repository import Notify
from bs4 import BeautifulSoup
from urllib import urlopen
#import for alternative notify
#import subprocess

def searchTureng(word):
    url="http://www.tureng.com/search/"+word
    try:
        answer = urlopen(url)
    except:
        return "No connection"
    html = answer.read()
    soup = BeautifulSoup(html)
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
Notify.init ("SelecTra")
trlated=Notify.Notification.new ('W: '+selectedText, result)
trlated.show ()

#alternative notify
#subprocess.Popen(["notify-send", selectedText, result])
