# while 迴圈
n = 1
sum = 0 # 記錄累加的結果
while (n <= 100):
    sum += n
    n += 1
print(sum)

# for 迴圈
for x in [3,5,1]:    #將內容分別印出來
    print(x)
    
for y in "Hello":
    print(y)

for z in range(5):
    print(z)

for s in range(5,10):
    print(s)

sum = 0
for x in range(1,101):  # 1+2+3+....+100
    sum += x
print(sum)    