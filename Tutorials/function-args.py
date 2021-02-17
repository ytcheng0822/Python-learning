# 參數預設的資料
def power(base,exp):
    print(base**exp)  # 次方
power(3,2)
power(4,0)

# 使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(n2=2,n1=4)

# (無限/不定)參數資料
def avg(*nums):
    sum=0
    for n in nums:
        sum+=n
    print(sum/len(nums))
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)
