# break 的簡易範例     #(ctrl + /)可以快速把程式碼註解掉
# n=0
# while (n<5):
#     if (n==3):
#         break
#     print(n)
#     n+=1
# print("最後的n:",n)

# continue 的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if (x%2==0):   # x是偶數
#         continue
#     print(x)
#     n+=1
# print("最後的n:",n) # n為奇數個數

# # else 的簡易範例
# sum=0
# for n in range(11): # 0~10
#     sum+=n
# else:
#     print(sum)

# 綜合範例: 找出整數平方根
# ex: 輸入9 , 得到3
#     輸入11 ,得到(沒有)
# n=input("請輸入一個正整數:")
# n=int(n)
# for i in range(n):
#     if (n == i*i):
#         print("整數平方根為:",i)
#         break   # 用break強制結束迴圈時, 不會執行else區塊
# else:
#     print("沒有整數平方根")    