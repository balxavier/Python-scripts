#!python
# coding=utf-8

import os, sys, urllib, arexx

#Read the url parsed threw the browser menu

url = sys.argv[1]

#Extract Domain from url

from urllib.parse import urlparse
domain = urlparse(url).netloc

#Test the domain to determine the right script

def urldomain(domain):
        switcher={
                'www.twitch.tv':'twitch',
                'm.twitch.tv':'twitch',
                'www.youtube.com':'youtube',
                'youtu.be':'youtube',
                'www.youtube-nocookie.com':'youtube',
                'm.youtube.com':'youtube',
                'youtube.com':'youtube',
                'vimeo.com':'vimeo',
                'www.dailymotion.com':'dailymotion',
                'www.skaitv.gr':'skaitv',
                'dlive.tv':'dlive',
                'peertube.com:'peertube',
                'wasd.tv':'wasd',
                'lbry.tv':'lbry',
             }
         website = switcher.get(domain,"other")

#Notify the result

notifyarg1 = ' TITLE="' + website + ' video"'
notifyarg2 = ' IMG="Icones/' + website + '.png" IMGVALIGN=1'
arexx.dorexx("NOTIFYA", "REGISTERAPP APP=PYTHONNOTIFY" + notifyarg1 + notifyarg2 + "Now playing ...")

#Launch the correct script

if website == 'other':
  os.system('APPDIR:Mplayer -cache 8092 " + url
else:
  os.system('C:Python ' + website + '.py ' + '-shh -u " + url
  
areex.dorexx("NOTIFYA", "UNREGISTERAPP APP=PYTHONNOTIFY")
