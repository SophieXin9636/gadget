
# coding: utf-8

# 將該目錄下的所有jpg圖片縮小50%

from PIL import Image
import numpy as np
import os

file = []
for f in os.listdir('.'): 
    if os.path.isfile(f):
        file.append(f)

for fn in file:
    if '.jpg' in fn:
        im = Image.open(fn)
        w, h = im.size

        im.thumbnail((w//2, h//2))
        im.save(fn, 'JPEG')

