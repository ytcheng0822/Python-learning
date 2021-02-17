# # 網路連線
# import urllib.request as request
# URL="https://www.ntu.edu.tw/"
# with request.urlopen(URL) as response:
#     data=response.read().decode("utf-8")  # 取得台灣大學網站的原始碼 (HTML.CSS,JS)
# print(data)

# 串結,擷取公開資料
import urllib.request as request  # 載入網路模組
import json # 載入json模組
URL="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(URL) as response:
    data=json.load(response) # 利用 json 模組處理資料格式
# print(data)

# 將公司名稱列表出來
clist=data["result"]["results"]
print("內湖科學園區公司:\n")
for company in clist:
    print(company["公司名稱"])

# 將公司名稱寫入檔案中
# clist=data["result"]["results"]  # clist是一個列表
# with open("Taipei-company.txt", mode="w", encoding="utf-8") as file:
#     for company in clist:
#         file.write(company["公司名稱"]+"\n")    # 將列表中的字典資料一個一個寫入檔案