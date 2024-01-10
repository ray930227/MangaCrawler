功能
===
- [x] 根據輸入搜尋漫畫
- [x] 爬取漫畫圖片

需求
===
以下python需要安裝，否則程式無法運行
**requests** 
```
pip install requests
```
**bs4**
```
pip install bs4
```
**progress**
```
pip install progress
```

安裝
===
**取得專案**  
```
git clone git@github.com:ray930227/MangaCrawler.git
```
- 請確保專案路徑不包含中文

運行
===
**運行專案**  
```
python ./MangaCrawler.py <漫畫名稱>
```

**更新漫畫列表**  
```
python ./getMangaID.py
```
- 更新需花費長時間，設備不好不建議更新，github上的mangaList會不定期更新，直接下載覆蓋即可
