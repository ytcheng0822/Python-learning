# 載入 numpy 模組
import numpy as np

# 逐元運算 (elementwise)
# data1 = np.array([3, 2, 6])    # 兩個資料量必須相同
# data2 = np.array([1, 3, 6])

# result = data1 + data2
# print("加法", result)

# result = data1 * data2
# print("乘法", result)

# result = data1 > data2
# print("是否大於", result)

# result = data1 == data2
# print("是否相等", result)


# 矩陣運素 (matrix)
# data1 = np.array([   # 1x2的矩陣
#     [1, 3]
# ])

# data2 = np.array([   # 2x3的矩陣
#     [2, -1, 3],
#     [-2, 4, 1]
# ])

# result = data1@data2  # 矩陣內積運算,得到 1x3 的矩陣
# print("內積", result)  # [[1x2 + 3x-2 , 1x-1 + 3x4 , 1x3 + 3x1]]

# result = np.outer(data1, data2)  # 矩陣外積運算, 得到 2x6 的矩陣
# print("外積", result)


# 統計運算 (statistics)
# data = np.array([    # 2x3 的二維陣列
#     [2, 1, 7],
#     [-5, 3, 8]
# ])

# result = data.sum()
# print("總和", result)   # 把全部的資料相加

# result = data.max()
# print("最大值", result)

# result = data.mean()
# print("平均數", result)

# result = data.std()
# print("標準差", result)

# result = data.sum(axis=0)  # 針對欄(column)做總和 (針對第一個維度做總和)
# print(result)              # 得到 1x3 的一維陣列

# result = data.sum(axis=1)  # 針對列(row)做總和    (針對第二個維度做總和)
# print(result)              # 得到 1x2 的一維陣列

# result = data.max(axis=0)  # 針對欄(column)找出最大值
# print(result)              # 得到 1x3 的一維陣列

# result = data.mean(axis=1) # 針對列(row)取平均
# print(result)              # 得到 1x2 的一維陣列


# 逐值累加
# data = np.array([    # 2x3 的二維陣列
#     [2, 1, 7],
#     [-5, 3, 8]
# ])

# result = data.cumsum()  # cumulative sum(累計的總和)
# print(result)

# result = data.cumsum(axis=0) # 針對欄(column)做逐值累加 (針對第一個維度做逐值累加)
# print(result)                       

# result = data.cumsum(axis=1) # 針對列(row)做逐值累加    (針對第二個維度做逐值累加)
# print(result)  