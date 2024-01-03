import requests
from bs4 import BeautifulSoup
import os

def getMangaID():
    with open(os.path.dirname(os.path.abspath(__file__))+'\\mangaList.txt', 'w',encoding='utf-8') as f:
        for i in range(1000,10000):
            print(i)
            url="https://www.cartoonmad.com/comic/"+str(i)+".html"
            html=requests.get(url)
            html.encoding = "big5"
            soup = BeautifulSoup(html.text, "html.parser")
            temp = soup.find_all("title")[0].text.strip()
            if temp!="動漫狂 - 免費動畫漫畫分享社群 !":
                f.write(str(i)+":"+temp[:-14]+"\n")
            else:
                f.write(str(i)+":None\n")

getMangaID()