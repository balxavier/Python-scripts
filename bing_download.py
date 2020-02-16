import os # import the os package

drawer = 'ram:'

os.system("wget -O ram:index.html http://www.bing.com") # download the bing index
str1 = open(drawer + 'index.html', 'r').read() # extract the file path using split
str2=str1.split('background-image: url(')[1]
str3=str2.split(".jpg")[0]
str4=str3.split('/th?id=OHR.')[1]
str5=str4.split('_FR-FR')[0]
str6=drawer + str5 + '.jpg'
os.system('wget -O ' + str6 + ' http://www.bing.com' + str3 + '.jpg') # donwload the daily image
