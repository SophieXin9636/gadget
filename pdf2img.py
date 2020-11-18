from pdf2image import convert_from_path, convert_from_bytes
import tempfile
import os


pdfPath = "/home/user/temp/"
imgPath = "/home/user/temp/img/"
file_list = os.listdir(pdfPath)

for file in file_list:
	if os.path.isdir(file):
		print(file)
		file_list.remove(file)
	if file.split('.')[1] != 'pdf':
		file_list.remove(file)
	#if 'pdf' not in file:
	#	file_list.remove(file)

print(file_list)

for file in file_list:
	if os.path.isdir(file):
		continue
	if file.split('.')[1] != 'pdf':
		continue
	images = convert_from_path(pdfPath + file)

	with tempfile.TemporaryDirectory() as path:
		images_from_path = convert_from_path(pdfPath + file, output_folder=path)
		for cnt, image in enumerate(images_from_path):
			if not os.path.exists(imgPath):
				os.makedirs(imgPath)
			new_file = imgPath+file.split('.')[0]
			if len(file_list) == 1:
				image.save(file.split('.')[0] + '.png')
				print(file.split('.')[0] + '.png')
			else:
				image.save(file.split('.')[0] + str(cnt+1) + '.png')
				print(file.split('.')[0] + str(cnt+1) + '.png')
		#print(images_from_path)