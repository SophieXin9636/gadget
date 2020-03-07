import os
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

dirName = './Desktop/myFolder/'
base_url = "https://your.page/" 
total_page = 100
extension = '.jpg'
os.makedirs(dirName, exist_ok=True)

for i in range(1,total_page+1):
    resp = requests.get(base_url + str(i) + extension)
    path = dirName + str(i) + extension

    with open(path, 'wb') as file:  
        if(resp.status_code == 200):
            file.write(resp.content)