import os

dirName = "/Desktop/myfolder/"
origin_typ = ".swf.png"
modify_typ = ".png"
size = 100 # number of downloaded page
for i in range(1,size+1):
    os.rename(dirName + str(i) + origin_typ,dirName + str(i) + modify_typ)