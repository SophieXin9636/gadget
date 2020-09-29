from pdf2image import convert_from_path, convert_from_bytes
import tempfile
import os

pdfPath = "/home/user/temp/"
imgPath = "/home/user/temp/img"
file_list = os.listdir(pdfPath)
print(file_list)
for file in file_list:
	if os.path.isdir(file):
		continue
	if file.split('.')[1] != 'pdf':
		continue
	images = convert_from_path(pdfPath + file)

	with tempfile.TemporaryDirectory() as path:
		images_from_path = convert_from_path(pdfPath + file, output_folder=path)
		for image in images_from_path:
			if not os.path.exists(imgPath):
				os.makedirs(imgPath)
			new_file = imgPath+file.split('.')[0]
			image.save(file.split('.')[0] + '.png')
			print(file.split('.')[0] + '.png')
		#print(images_from_path)