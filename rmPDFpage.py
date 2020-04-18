# pip3 install PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader 
pages_to_keep = [1,2,3,4,5,6,7,8] # page numbering starts from 0 
infile = PdfFileReader('myfile.pdf', 'rb') 
outFile = PdfFileWriter() 

for i in range(infile.getNumPages()): 
    if i in pages_to_keep: 
     p = infile.getPage(i) 
     outFile.addPage(p) 

with open('newfile.pdf', 'wb') as f: 
    outFile.write(f)
