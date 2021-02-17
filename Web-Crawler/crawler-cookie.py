# 抓取 PTT_Gossiping 的網頁原始碼(HTML)
import urllib.request as req
def getData(url):   # 因為要一次抓取很多頁面,所以用函式包裝程式
    # 建立一個Request物件,附加Request Headers的資訊,讓網站sever覺得我們是正常的使用者
    request=req.Request(url, headers={
        "cookie":"over18=1",    # 加上cookie讓網站知道我們已經滿18歲
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    from bs4 import BeautifulSoup
    soup=BeautifulSoup(data,"html.parser")
    titles=soup.find_all("div", class_="title")  # 抓取標題包含<div>標籤的資料
    for title in titles:
        if (title.a != None):     # 如果標題包含<a>標籤(沒有被刪除),就印出來
            print(title.a.string)

    # 抓取上一頁的連結
    nextlink=soup.find("a", string="‹ 上頁") # 找到內文是‹ 上頁的<a>標籤
    return nextlink["href"]


# 主程式:連續抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while (count<5):
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1