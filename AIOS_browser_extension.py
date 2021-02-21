#!python
# coding=utf-8
# AIOStreams browser menu extension for AmigaOS
# v1.0

import os, sys, myurlparse, arexx

AIOSpath = os.path.dirname(__file__)

#Read the url parsed threw the browser menu

url = sys.argv[1]

#Extract Domain from url

from myurlparse import urlparse
domain = urlparse(url).netloc

#Test the domain to determine the right script

switcher = {
	'www.twitch.tv': "twitch",
	'm.twitch.tv': "twitch",
	'www.youtube.com': "youtube",
	'youtu.be': "youtube",
	'www.youtube-nocookie.com': "youtube",
	'm.youtube.com': "youtube",
	'youtube.com': "youtube",
	'vimeo.com': "vimeo",
	'www.dailymotion.com': "dailymotion",
	'www.skaitv.gr': "skaitv",
	'dlive.tv': "dlive",
	'peertube.com': "peertube",
	'wasd.tv': "wasd",
	'lbry.tv':"lbry"
	}

website = switcher.get(domain, "other")

#Notify the result

notifyarg = 'SCREEN="FRONT" PRI=9 IMG="' + AIOSpath + '/Icones/' + website + '.png" TITLE="' + website + ' video" IMGVALIGN=1 Now Playing...'
arexx.dorexx("NOTIFYA", "REGISTERAPP APP=PYTHONNOTIFY")
arexx.dorexx("NOTIFYA", 'NOTIFY APP=PYTHONNOTIFY ' + notifyarg)

#Launch the correct script

if website == 'other':
	os.system('APPDIR:Mplayer -cache 8092 ' + url)
else:
	os.system('C:Python ' + AIOSpath + '/' + website + '.py ' + '-shh -u ' + url)
  
arexx.dorexx("NOTIFYA", "UNREGISTERAPP APP=PYTHONNOTIFY")
