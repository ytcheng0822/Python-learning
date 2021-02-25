# 載入 numpy 模組
import numpy as np

# 多維陣列維度/形狀操作
# 觀察資料形狀(shape)
# data = np.ones(10)  # [1,1,1,1,1,1,1,1,1,1]
# print(data.shape)

# data = np.array([
#     [3,1,5],
#     [1,2,3]
# ])
# print(data.shape)


# 資料轉置(T)
# data = np.array([
#     [2,4,1],
#     [1,5,0]
# ])
# print(data.shape)    # (2,3)
# print(data.T.shape)  # (3,2)


# 扁平化資料
# data = np.array([      # (2,2,3)
#     [
#         [1,2,3],[4,5,6]
#     ],
#     [
#         [7,8,9],[9,8,10]
#     ]
# ])
# newData = data.ravel()   # 回傳扁平化後的資料,放到新的變數裡
# print(newData)
# print(newData.shape)


# 重塑資料形狀
# data = np.array([      # (2,2,3) ==> 2x2x3=12
#     [
#         [1,2,3],[4,5,6]
#     ],
#     [
#         [7,8,9],[9,8,10]
#     ]
# ])
# newData = data.reshape(4,3)   # (4,3) ==> 4x3=12
# print(newData)

# newData = data.reshape(1,2,6)
# print(newData)
# print(newData.shape)


# data = np.zeros(18).reshape(3,6)
# print(data)

# data = np.arange(9).reshape(3,3)
# print(data)
# print(data.T)