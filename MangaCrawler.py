import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import sys

projectPath=os.path.dirname(os.path.abspath(__file__))

class Manga:
    def __init__(self,ID,Name,Chapter):
        self.ID=ID
        self.Name=Name
        self.Chapter=Chapter
        
mangaList=[]

def getMangaMainPageHtml(ID):
    url="https://www.cartoonmad.com/comic/"+str(ID)+".html"
    html=requests.get(url)
    html.encoding = "big5"
    return html

def getMangaChapterImage(manga,ch):
    if manga.Chapter.get(ch)==None:
        return False
    path = projectPath+"\\mangaImage\\"
    if not os.path.isdir(path):
        os.mkdir(path)
    path+=str(manga.ID)
    if not os.path.isdir(path):
        os.mkdir(path)
    path+="\\"+str(ch)
    if not os.path.isdir(path): 
        os.mkdir(path)
        for i in range(1,manga.Chapter[ch]+1):
            url="https://cc.fun8.us//2e5fc/"+str(manga.ID)+"/"+str(ch).zfill(3)+"/"+str(i).zfill(3)+".jpg"
            dir=path+"\\"+str(i)+".jpg"
            try:
                urllib.request.urlretrieve(url,dir)
            except:
                pass
    return True

def getMangaChapterImageURL(manga,ch):
    for i in range(1,manga.Chapter[ch]+1):
        url="https://cc.fun8.us//2e5fc/"+str(manga.ID)+"/"+str(ch).zfill(3)+"/"+str(i).zfill(3)+".jpg"

def getMangaByID(ID):
    for i in mangaList:
        if i.ID==ID:
            return i
    with open(projectPath+'\\mangaList.txt', 'r',encoding='utf-8') as f:
        for i in f.readlines():
            temp=i.strip().split(":")
            if int(temp[0])==ID:
                chapter=dict()
                if temp[1]!="None":
                    html=getMangaMainPageHtml(int(temp[0]))
                    soup=BeautifulSoup(html.text,"html.parser")
                    findAll = soup.find_all("table",width="800",align="center")[0].text.strip()
                    for j in findAll.split("•")[1:]:
                        tempChapter=j.split(" ")
                        chapter[int(tempChapter[1])]=int(tempChapter[3][1:tempChapter[3].find("頁")])
                mangaList.append(Manga(int(temp[0]),temp[1],chapter))
                return mangaList[-1]
    return None

def getMangaByName(Name):
    with open(projectPath+'\\mangaList.txt', 'r',encoding='utf-8') as f:
        for i in f.readlines():
            temp=i.strip().split(":")
            if temp[1]==Name:
                return getMangaByID(int(temp[0]))
    return None

def searchMangaByName(Name):
    result=[]
    with open(projectPath+'\\mangaList.txt', 'r',encoding='utf-8') as f:
        for i in f.readlines():
            temp=i.strip().split(":")
            if temp[1].find(Name)!=-1:
                result.append(temp[1])
    return result

def main():
    if len(sys.argv)<2:
        print('No argument')
        sys.exit()
    if len(sys.argv)>2:
        print('Incorrect argument')
        sys.exit()
    search=searchMangaByName(sys.argv[1])
    if(len(search)==0):
        print(sys.argv[1],"not found.")
    else:
        for i in range(len(search)):
            print(i+1,":",search[i],sep="")
        print("choose one")
        manga=getMangaByName(search[int(input())-1])
        chapterList=[i for i in manga.Chapter.keys()]
        print(manga.Name,"'s Chapters range is ",chapterList[0],"~",chapterList[-1],sep="")
        print("Choose one Chapter.")
        chapter=int(input())
        if chapter<chapterList[0] or chapter>chapterList[-1]:
            print(chapter,"not in range.")
        else:
            print("please wait.")
            if getMangaChapterImage(manga,chapter):
                print(f"Download in \"MangaImage\\{manga.ID}\\{chapter}\" completed.")
            else:
                print("Download failed.")
main()