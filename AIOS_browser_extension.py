#!python
# coding=utf-8
# AIOStreams browser menu extension for AmigaOS
# v1.1

import os, sys, asl, myurlparse, arexx, AIOSsites, vqw

AIOSpath = os.path.dirname(__file__)

#Read the url parsed threw the browser menu

url = sys.argv[1]

#Extract Domain from url

from myurlparse import urlparse
domain = urlparse(url).netloc

#Test the domain to determine the right script

website = AIOSsites.switcher.get(domain, "other")

#Notify the result

notifyarg = 'SCREEN="FRONT" PRI=9 IMG="' + AIOSpath + '/Icones/' + website + '.png" TITLE="' + website + ' video" IMGVALIGN=1 Now Playing...'
arexx.dorexx("NOTIFYA", "REGISTERAPP APP=PYTHONNOTIFY")
arexx.dorexx("NOTIFYA", 'NOTIFY APP=PYTHONNOTIFY ' + notifyarg)

#Launch the correct script

#Ask for quality
if website == 'twitch':
	vqualitylist = ' | '.join(str(n) for n in vqw.twitchVQW)
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
	vquality = str(vqw.twitchVQW[response-1])
elif website == 'youtube':
	vqualitylist = ' | '.join(str(n) for n in vqw.ytVQW)
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
	vquality = str(vqw.ytVQW[response-1])
elif website == 'vimeo':
	vqualitylist = ' | '.join(str(n) for n in vqw.vimeoVQW)
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
	vquality = str(vqw.vimeoVQW[response-1])
elif website == 'dailymotion':
	vqualitylist = ' | '.join(str(n) for n in vqw.dailymotionVQW)
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
	vquality = str(vqw.dailymotionVQW[response-1])
elif website == 'skaitv':
	vqualitylist = ' | '.join(str(n) for n in vqw.skaiVQW)
#	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
#	vquality = str(vqw.skaiVQW[response-1])
elif website == 'dlive':
	vqualitylist = ' | '.join(str(n) for n in vqw.dliveVQW)
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
	vquality = str(vqw.dliveVQW[response-1])
elif website == 'peertube':
	vqualitylist = ' | '.join(str(n) for n in vqw.peertubeVQW)
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
	vquality = str(vqw.peertubeVQW[response-1])
elif website == 'wasd':
	vqualitylist = ' | '.join(str(n) for n in vqw.twitchVQW)
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", vqualitylist)
	vquality = str(vqw.wasdVQW[response-1])
else :
	response = asl.MessageBox("Quality choice", "Please select a video quality: ", 'Default')

if website == 'other':
	os.system('APPDIR:Mplayer -cache 8092 ' + url)
elif website == 'skaitv':
	os.system('C:Python ' + AIOSpath + '/' + website + '.py ' + '-shh -u ' + url)
else:
	os.system('C:Python ' + AIOSpath + '/' + website + '.py ' + '-shh -u ' + url + ' -q ' + vquality)

arexx.dorexx("NOTIFYA", "UNREGISTERAPP APP=PYTHONNOTIFY")
