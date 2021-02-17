#有序可變動列表 List 用[]
grades=[12,60,15,70,90]
grades=grades+[100,110] #在列表後面加上資料
length=len(grades) #取得列表中的長度 len(列表名稱)
print(length)
grades[1:4]=[] #刪除列表中的60,15,70
print(grades[1:4]) #取列表中的60,15,70
grades[0]=55     #把55放到列表中的第一個位置
print(grades)

data=[[3,4,5],[6,7,8]]
print(data)
data[0][0:2]=[1,2,3,4]
print(data)

#有序不可變動列表 Tuple 用()
data=(3,4,5)
#data[0]=5    #Error:Tuple的資料不可以變動
data=data+(6,7)  #Tuple可以增加資料
print(data)