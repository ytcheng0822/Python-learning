import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)   # 0 ~ 10 之間產生50個點

y = x**2 + 2*x + 1         # 一元二次方程式

plt.plot(x,y)              # 座標軸顯示

plt.show()                 # 將圖顯示出來