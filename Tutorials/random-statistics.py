# 隨機模組
# import random

# 隨機選取
# data = random.choice([1,5,6,10,20]) # 從列表中隨機選取資料  choice=選取
# data = random.sample([1,5,6,10,20], 3) # 從列表中隨機選取3筆資料  sample=取樣
# print(data)

# 隨機調換順序
# data=[1,5,8,20]
# random.shuffle(data)  # 將列表的資料(in place)隨機調換順序  shuffle=洗牌
# print(data)

# 隨機取得亂數
# data=random.random()  # 0.0 ~ 1.0 之間的隨機浮點數亂數
# print(data)
# data=random.randint(1, 100) # 1 ~ 100 之間的隨機整數亂數
# print(data)
# data=int(random.uniform(10, 50)) # 自定義隨機亂數區間 10 ~ 50
# print(data)

# 取得常態分配亂數
# 平均數 100, 標準差 10 ,得到的資料【多數】在 90 ~ 110 之間
# data=random.normalvariate(100, 10)
# print(data)

# 平均數 0 , 標準差 5 ,得到的資料【多數】在 -5 ~ 5 之間
# data=random.normalvariate(0, 5)
# print(data)


# 統計模組
# import statistics as stat
# data=stat.mean([1,4,5,8])  # 取得平均數 ,mean=平均
# print(data)

# data=stat.median([1,3,5,7])  # 取得中位數 ,median=中間
# print(data)

# data=stat.stdev([1,2,3,4,5]) # 取得標準差 ,stdev(Standard Deviation)=標準偏差
# print(data)