# # Point 實體物件的設計: 平面座標上的點
# class Point: # 建立類別名稱
#     def __init__(self,x,y): # 定義初始化函式
#         self.x = x
#         self.y = y
#     def show(self):  # 定義實體方法
#         print(self.x, self.y)
#     def distance(self, targetX, targetY):  # 定義實體方法
#         return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5

# p=Point(3,4) # 建立實體物件
# p.show()     # 呼叫實體方法(Instance methods)
# result=p.distance(0,0) # 計算座標(3,4) 和 座標(0,0)之間的距離
# print(result)


# # File 實體物件的設計: 包裝檔案讀取的程式
# class File:
#     def __init__(self, name):
#         self.name = name
#         self.file = None  # 尚未開啟檔案所以一開始是 None
#     def open(self):
#         self.file = open(self.name, mode="r", encoding="utf-8")
#     def read(self):
#         return self.file.read()
#     def close(self):
#         self.file.close()

class File:
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案所以一開始是 None
    def open_and_read(self):
        with open(self.name, mode="r", encoding="utf-8") as self.file:
            return self.file.read()
# 讀取第一個檔案
f1 = File("data1.txt")
data = f1.open_and_read()
print(data)

# 讀取第二個檔案
f2 = File("data2.txt")
data = f2.open_and_read()
print(data)
