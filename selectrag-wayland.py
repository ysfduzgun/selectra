#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf-8
# Yusuf Duzgun yzduzgun@gmail.com
# Modified by Ali Riza Keskin
# License : GPL3

import os, sys
from urllib.request import Request, urlopen
import json
import urllib.parse
import subprocess

#lang = os.environ["LANG"].split("_")[0]
lang = "tr"

#https://translate.google.com/?sl=en&tl=tr&text=LICENSE&op=translate
#https://translate.google.com/details?sl=en&tl=tr&text=LICENSE&op=translate
#"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl="+lang return data[0][0]

def searchGoogle(word):
    url="https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl="+lang
    data = ""
    post =  urllib.parse.urlencode({'q': word}).encode()
    req = Request(url, data=post, headers={'User-Agent': 'Mozilla/5.0'}, method="POST")
    data = urlopen(req).read()
    data = json.loads(data.decode('utf-8'))
    return data[0]

if len(sys.argv) > 1:
    selectedText = sys.argv[1]
else:
    selectedText = os.popen('wl-paste -p').read()

result = searchGoogle(selectedText)
subprocess.Popen(["notify-send", "SelecTra", result])
