import threading    # 導入執行緒模組
import time         # 導入時間模組
from queue import Queue   # 導入佇列模組(FIFO)

def job1(num, Q):
    for i in range(num):
        print("job1 send", i, "to job2")
        Q.put(i)
        time.sleep(1)

def job2(num, Q):
    for i in range(num):
        data = Q.get()
        print("job2 receive", data)
        time.sleep(1)

Q = Queue()

t1 = threading.Thread(target=job1, args=(3, Q))   # 程式一開始會先從start()開始
t1.start()                                        # 當某執行緒閒置或等待時,就會切換到其他執行緒工作

t2 = threading.Thread(target=job2, args=(5, Q))
t2.start()

for i in range(2):
    print("Main send", i+10, "to job2")  # 如果job接收到10、11就是Main thread送的
    Q.put(i+10)
    time.sleep(1)
  

t1.join()      # 等待t1和t2都執行結束
t2.join()
print("Finish")  # 才印出Finish