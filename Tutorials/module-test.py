# 載入內建的 sys 模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

# 建立 geometry 模組,只能在同一個資料夾才能直接使用
# import geometry
# result = geometry.distance(1,1,5,5)   #計算距離
# print(result)
# result = geometry.slope(1,2,5,6)      #計算斜率
# print(result)

# 調整搜尋模組的路徑 Problems:(CTRL + SHIFT + P > Select linter > Disabled Linter)
# 新增路徑是一次性的,程式跑完就沒了

# import sys
# sys.path.append("Tutorials//modules")  # 在模組的搜尋路徑列表中【新增路徑】
# print(sys.path)  # 印出模組搜尋路徑列表
# print("----------------------------")
# import modules.geometry as geometry
# print(geometry.distance(1,1,5,5))