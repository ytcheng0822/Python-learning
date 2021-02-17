# 抓取 PTT_movie 的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

# 建立一個Request物件,附加Request Headers的資訊,讓網站sever覺得我們是正常的使用者
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)


# 解析原始碼, 取得每篇文章的標題 (安裝第三方套件) pip install beautifulsoup4
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(data,"html.parser") # 讓BeautifulSoup協助我們解析HTML格式文件
# print(soup.title.string)
# titles=soup.find("div", class_="title") # 尋找 class="title" 的 <div> 標籤
# print(titles.a.string)

from bs4 import BeautifulSoup
soup=BeautifulSoup(data,"html.parser")
titles=soup.find_all("div", class_="title")  # 抓取標題包含<div>標籤的資料
for title in titles:
    if (title.a != None):     # 如果標題包含<a>標籤(沒有被刪除),就印出來
        print(title.a.string)