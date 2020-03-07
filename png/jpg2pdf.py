from PIL import Image

dirName = "/Desktop/myfolder/"
size = 100 # number of downloaded page

imglist = []
image1 = Image.open(dirName +'1.png')
im1 = image1.convert('RGB')
for i in range(2,total_page+1):
    image2 = Image.open(dirName + str(i) +'.png')
    im2 = image2.convert('RGB')
    imglist.append(im2)
im1.save(dirName + 'my.pdf', save_all=True, append_images=imglist)