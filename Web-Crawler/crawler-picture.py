import requests
from bs4 import BeautifulSoup
import shutil

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}

res = requests.get("https://85st.com/thread-1323572-1-1.html",headers=headers)

soup = BeautifulSoup(res.text,"html.parser")

for img in soup.select(".zoom"):
    fname = img["zoomfile"].split("/")[-1]
    res2 = requests.get("https://85st.com/"+img["zoomfile"], stream=True)
    f = open(fname, "wb")
    shutil.copyfileobj(res2.raw, f)
    f.close()
    del res2