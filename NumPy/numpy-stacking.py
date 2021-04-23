import numpy as np
# 準備測試資料
arr1 = np.array([    # 2x3
    [1,2,3],
    [4,5,6]
])

arr2 = np.array([    # 2x3
    [7,8,9],
    [10,11,12]
])

arr3 = np.array([    # 2x2
    [13,14],
    [15,16]
])

# 合併第二個維度
result3 = np.hstack((arr1, arr2, arr3))
print(result3)

"""
    2x8
    [
        [1,2,3,7,8,9,13,14],
        [4,5,6,10,11,12,15,16]
    ]
"""



# 合併第一個維度
# result1 = np.vstack((arr1, arr2))
# print(result1)
"""
    4x3
    [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
    ]
"""

# 合併第二個維度
# result2 = np.hstack((arr1, arr2))
# print(result2)

"""
    2x6
    [
        [1,2,3,7,8,9],
        [4,5,6,10,11,12]
    ]
"""
