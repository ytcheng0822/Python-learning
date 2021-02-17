#集合的運算 用{}
s1={3,4,5}
print(3 in s1)    #判斷3是否在s1
print(10 in s1)   
print(10 not in s1)  #判斷10是否 沒有在s1

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2     #交集:取兩個集合中,相同的資料
s3=s1|s2     #聯集:取兩個集合中的所有資料,但不重複
s3=s1-s2     #差集: 從s1中, 減去和s2重疊的部分 
s3=s1^s2      #反交集:取兩個集合中,不重疊的部分
print(s3)

s=set("Hello") #把字串中的字母拆解成集合 set(字串)
print(s)
print("H" in s)
print("A" in s)

#字典的運算: key-value 配對
dict={"apple":"蘋果","banana":"香蕉"}
dict["apple"]="小蘋果"
print(dict["apple"])
print("apple" in dict)  #判斷key是否存在
print("watermelon" in dict)
print(dict)
del dict["apple"]  #刪除字典中的鍵值對(key-value pair)
print(dict)

dict={x:x*2 for x in [1,2,3]}
print(dict)