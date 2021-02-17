# 載入 pandas 模組
import pandas as pd
# 建立 Series (單維度資料分析)
# data=pd.Series([20, 10, 15])

# 基本 Series 操作
# print(data)
# print("Max",data.max())   # 印出最大值
# print("Mediam",data.median())   # 印出中位數

# data=data*2
# print(data)  # 將data中的數字x2

# data=(data==20)    # 如果data內的資料是20 就是True, 不是則Flase
# print(data)


# 建立 DataFrame (雙維度資料分析)
# data=pd.DataFrame({
#     "name":["Chris","Tim","John"],   # 第一欄 name
#     "salary":[50000,35000,45000]     # 第二欄 salary
# })
# 基本 DataFrame 操作
# print(data)

# 取得特定的欄位
# print(data["name"])

# 取得特定的列
# print(data)
# print("=================")
# print(data.iloc[0])  # 印出第一列