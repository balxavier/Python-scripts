import os, time # import the os package
from PIL import Image, ImageFilter

drawer = 'ram:T/'
file = 'daily_im.jpg'
WPfile = 'WBWallpaper_'
WTfile = 'WBTitlebar_'

os.system("wget -O ram:T/index.html http://www.bing.com") # download the bing index
str1 = open(drawer + 'index.html', 'r').read() # extract the file path using split
str2=str1.split('background-image: url(')[1]
str3=str2.split(".jpg")[0]
os.system('wget -O ram:T/daily_im.jpg http://www.bing.com' + str3 + '.jpg') # donwload the daily image

print('Preparing theme, please wait ...')

if os.path.isfile(drawer + WPfile +file):
	WPfile = 'WBWallpaper2_'; WTfile = 'WBTitlebar2_'

titlebar_height = 26
screen_height = 1080
screen_width = 1920

image_original = Image.open(drawer + file)

def crop_wbtitlebar(image_path, coords, saved_location):

	image_obj = image_original.resize((screen_width / 24, screen_height / 24), Image.ANTIALIAS)
	image_obj = image_obj.filter(ImageFilter.GaussianBlur(2))
	image_obj = image_obj.resize((screen_width, screen_height), Image.ANTIALIAS)
	image_obj.save('ram:T/LockscreenBG.jpg', subsampling=0, quality=100)
	cropped_image = image_obj.crop(coords)
	cropped_image.save(saved_location, subsampling=0, quality=100)

def crop_wbpattern(image_path, coords, saved_location):

	image_obj = image_original.resize((screen_width, screen_height), Image.ANTIALIAS)
	cropped_image = image_obj.crop(coords)
	cropped_image.save(saved_location, subsampling=0, quality=100)

if __name__ == '__main__':
	crop_wbtitlebar(drawer, (0, 0, screen_width, titlebar_height),drawer+ WTfile + file)
	crop_wbpattern(drawer, (0, titlebar_height, screen_width, screen_height),drawer+ WPfile + file)

os.remove("ram:T/index.html")
os.remove("ram:T/daily_im.jpg")

if WPfile == 'WBWallpaper_':
	os.system('copy VIDE:Modern/Bing/1/#?.prefs TO env:sys QUIET')
if WPfile == 'WBWallpaper2_':
	os.system('copy VIDE:Modern/Bing/2/#?.prefs TO env:sys QUIET')

print('Purging tempory files')
time.sleep(5)
if WPfile == 'WBWallpaper_':
	if os.path.isfile(drawer + 'WBWallpaper2_' +file):
		os.remove("ram:T/WBWallpaper2_daily_im.jpg"); os.remove("ram:T/WBTitlebar2_daily_im.jpg")
if WPfile == 'WBWallpaper2_':
	os.remove("ram:T/WBWallpaper_daily_im.jpg"); os.remove("ram:T/WBTitlebar_daily_im.jpg")
exit