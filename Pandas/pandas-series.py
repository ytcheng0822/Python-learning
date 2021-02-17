# 載入 pandas 模組
import pandas as pd

# 資料索引
data=pd.Series([5, 4, -2, 3, 7], index=["a", "b", "c", "d", "e"])
print(data)

# 觀察資料
# print("資料型態", data.dtype)
# print("資料數量", data.size)
# print("資料索引", data.index)

# 取得資料: 根據順序, 根據索引
# print(data[2], data[0])
# print(data["e"], data["d"])

# 數字運算: 基本, 統計, 順序
# print("最大值", data.max())
# print("總和", data.sum())
# print("全部相乘", data.prod())
# print("平均值", data.mean())
# print("標準差", data.std())
# print("中位數", data.median())
# print("最大的三個數", data.nlargest(3))
# print("最小的二個數", data.nsmallest(2))

# data=pd.Series(["您好", "Python", "Pandas"])
# 字串運算: 基本, 串接, 搜尋, 取代
# print(data.str.lower())   # 全部變小寫字母
# print(data.str.len())     # 算出每個字串的長度
# print(data.str.cat(sep="-")) # 把字串串起來, 可以自訂串接的符號
# print(data.str.contains("P"))  # 判斷每個字串中是否含有"P"
# print(data.str.replace("您好", "Hello"))  # 更換資料