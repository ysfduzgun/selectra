#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
# Yusuf Duzgun ysfduzgun92@gmail.com
# Licanse : GPL3





import os
from gi.repository import Notify
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
#import unidecode

def searchTureng(word):	
	url="http://www.tureng.com/search/"+word	
	try:
		answer = urlopen(url)
	except:
		return "No connection"
	html = answer.read()
	parsedHtml = BeautifulSoup(html)
	trlated = parsedHtml.body.find('td', attrs={'class':'tr ts'}).text
	trlated.encode("ascii", "ignore")


	return trlated



selectedText = os.popen('xsel').read()
print (selectedText)

result = searchTureng(selectedText)
print (result)

Notify.init ("SelecTra")
trlated=Notify.Notification.new ("SelecTra", result)
trlated.show () 



