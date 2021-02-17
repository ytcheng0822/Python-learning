# Point 實體物件的設計: 平面座標上的點
# 第一步驟先建立類別class
class Point:
    def __init__(self,x,y):  # 定義初始化函式,透過(self)來定義實體屬性
        self.x=x         # 定義實體屬性(Instance Attribute)
        self.y=y

# 建立第一個實體物件(Instance object1)
p1=Point(3,4)
print(p1.x, p1.y)

# 建立第二個實體物件(Instance object2)
p2=Point(5,6)
print(p2.x,p2.y)


# FullName 實體物件的設計: 分開紀錄姓,名資料的全名
class FullName:
    def __init__(self,first,last): # 想利用類別建立實體物件,就必須透過初始化函式
        self.first=first
        self.last=last

name1=FullName("Yu-Ting","Cheng")
print(name1.first, name1.last)

name2=FullName("Y.T.","Cheng")
print(name2.first, name2.last)