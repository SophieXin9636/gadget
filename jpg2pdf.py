from PIL import Image

dirName = "./"
size = 1 # number of downloaded page

imglist = []
image1 = Image.open(dirName +'2.png')
im1 = image1.convert('RGB')
if size > 1:
	for i in range(2,size+1):
	    image2 = Image.open(dirName + str(i) +'.png')
	    im2 = image2.convert('RGB')
	    imglist.append(im2)
im1.save(dirName + 'my.pdf', save_all=True, append_images=imglist)