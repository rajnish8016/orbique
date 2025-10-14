import requests
from bs4 import BeautifulSoup
url="https://wallhaven.cc/"
response=requests.get(url)
if response.status_code==200:
    soup=BeautifulSoup(response.content,"html.parser")
    test =soup.find_all("h1",class_="logo")

    for i in test:
        print(i)
    