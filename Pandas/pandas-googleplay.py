import pandas as pd

# 讀取資料
data = pd.read_csv("E:\Python-learning\Pandas\googleplaystore.csv")  # 把 csv 格式的檔案讀取成一個 DataFrame

# 觀察資料
print("資料數量", data.shape)
print("資料欄位", data.columns)
print("==================================================================================")


# 分析資料:評分的各種統計數據
# print(data["Rating"])
# condition = data["Rating"] <= 5    # 排除掉不乾淨的資料,留下最正確的資料
# data = data[condition]
# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得前1000個應用程式的平均分數", data["Rating"].nlargest(1000).mean())


# 分析資料:安裝數量的各種統計數據
# print(data["Installs"])
# print(data["Installs"][10472])    # ValueError: Unable to parse string "Free" at position 10472
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "").replace("Free", ""))
# print("平均安裝數", data["Installs"].mean())
# condition = data["Installs"] > 100000
# print("安裝數量大於 100000 的應用程式有幾個", data[condition].shape[0])  # (4950, 13)--> shape[0]=4950


# 基於資料的應用:關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字: ")
condition = data["App"].str.contains(keyword, case = False)  # case = False (忽略大小寫)
# print(data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition]["App"].shape[0])  # 取得數量用 shape[0]