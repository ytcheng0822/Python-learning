# 儲存檔案    # 開啟含有中文的檔案用 encoding="utf-8"
# file=open("data.txt", mode="w", encoding="utf-8")  # 開啟
# file.write("測試中文\n今天是2021/02/05")  # 寫入
# file.close()  # 關閉
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("今天是2021/02/05\n最佳開檔方式,不需要file.close()")
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("6\n4")

# 讀取檔案
# 把檔案中的數字資料,一行一行的讀出來,並計算總合
# sum=0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file:   # 一行一行的讀取
#         sum+=int(line)  # 將line轉換成int格式
# print(sum)

# 附加檔案
# with open("data.txt", mode="a", encoding="utf-8") as file:
#     file.write("\n添加文字內容")


# 使用 json 格式讀取,覆寫檔案
# import json
# with open("config.json", mode="r") as file:
#     data=json.load(file) # 從檔案中讀取json資料,放入變數data裡面
# print(data)  # data 是一個字典資料
# # print("name:",data["name"])
# # print("version:",data["version"])
# data["name"]="Tim"  # 修改變數中的資料

# # 把最新的資料覆寫回檔案中
# with open("config.json", mode="w") as file:
#     json.dump(data,file)