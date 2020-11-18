from PIL import Image
import os

imgPath = "/home/user/Desktop/"
pdfPath = "/home/user/Desktop/"

output_filename = "my.pdf"

file_list = os.listdir(imgPath)

for file in file_list:
	if not os.path.isfile(file):
		file_list.remove(file)
	if file.split('.')[1] != "png" and file.split('.')[1] != "jpg":
		file_list.remove(file)

print("File list: ")
print(file_list)

size = len(file_list) # number of downloaded page
imglist = []
image1 = Image.open(imgPath + file_list[0])
im1 = image1.convert('RGB')

for cnt, file in enumerate(file_list):
	if cnt == 0:
		continue
	#if not imglist: # imglist is empty
	image2 = Image.open(imgPath + file)
	im2 = image2.convert('RGB')
	imglist.append(im2)
im1.save(imgPath + output_filename, save_all=True, append_images=imglist)