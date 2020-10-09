import os, time # import the os package
import asl
from PIL import Image, ImageFilter

WPfile = 'WBWallpaper.jpg'
WTfile = 'WBTitlebar.jpg'

(drawer, file) = asl.FileRequest(title="Please select a Picture to set as Wallpaper", drawer='RAM:', filename="", pattern="#?")

if drawer.endswith(':'):
	drawer = drawer
else:
	drawer = drawer + '/'

print('image en traitement ... ' + drawer+file)
print('Preparing theme, please wait ...')

if os.path.isfile('Ram:T/WBwallpaper.jpg'):
	WPfile = 'WBWallpaper2.jpg'; WTfile = 'WBTitlebar2.jpg'

titlebar_height = 26
screen_height = 1080
screen_width = 1920

image_original = Image.open(drawer + file)
image_obj_w, 	image_obj_h = image_original.size
print(image_obj_w, 	image_obj_h)

if float(image_obj_w) / image_obj_h > float(screen_width) / screen_height:
	divider = float(screen_height) / image_obj_h
else:
	divider= float(screen_width) / image_obj_w

print(divider)

image_original = image_original.resize((int(image_obj_w*divider), int(image_obj_h*divider)), Image.ANTIALIAS)
image_obj_w, 	image_obj_h = image_original.size
print(image_obj_w, 	image_obj_h)

def crop_tempory(image_path, coords, saved_location):

	image_obj = image_original
	cropped_image = image_obj.crop(coords)
	cropped_image.save(saved_location, subsampling=0, quality=100)
	print('Tempory image done')

def crop_wbtitlebar(image_path, coords, saved_location):
	
	image_obj = Image.open('Ram:T/Tempory.jpg')
	image_obj = image_obj.resize((screen_width / 24, screen_height / 24), Image.ANTIALIAS)
	image_obj = image_obj.filter(ImageFilter.GaussianBlur(2))
	image_obj = image_obj.resize((screen_width, screen_height), Image.ANTIALIAS)
	image_obj.save('ram:T/LockscreenBG.jpg', subsampling=0, quality=100)
	cropped_image = image_obj.crop(coords)
	cropped_image.save(saved_location, subsampling=0, quality=100)
	print('WBTitleBar image done')

def crop_wbpattern(image_path, coords, saved_location):

	image_obj = Image.open('Ram:T/Tempory.jpg')
	cropped_image = image_obj.crop(coords)
	cropped_image.save(saved_location, subsampling=0, quality=100)
	print('WBWallpaper image done')

if __name__ == '__main__':
	crop_tempory(drawer, (int(image_obj_w) / 2 - screen_width / 2, int(image_obj_h) / 2 - screen_height / 2, int(image_obj_w) / 2 + screen_width / 2, int(image_obj_h) / 2 + screen_height / 2), 'Ram:T/Tempory.jpg')
	crop_wbtitlebar('Ram:T/', (0, 0, screen_width, titlebar_height),'Ram:T/' + WTfile)
	crop_wbpattern('Ram:T/', (0, titlebar_height, screen_width, screen_height),'Ram:T/' + WPfile)


os.remove("ram:T/Tempory.jpg")

if WPfile == 'WBWallpaper.jpg':
	os.system('copy VIDE:Modern/User/1/#?.prefs TO env:sys QUIET')
if WPfile == 'WBWallpaper2.jpg':
	os.system('copy VIDE:Modern/User/2/#?.prefs TO env:sys QUIET')

print('Purging tempory files')
time.sleep(5)
if WPfile == 'WBWallpaper.jpg':
	if os.path.isfile(drawer + 'Ram:/T/WBWallpaper2.jpg'):
		os.remove("ram:T/WBWallpaper2.jpg"); os.remove("ram:T/WBTitlebar2.jpg")
if WPfile == 'WBWallpaper2.jpg':
	os.remove("ram:T/WBWallpaper.jpg"); os.remove("ram:T/WBTitlebar.jpg")
