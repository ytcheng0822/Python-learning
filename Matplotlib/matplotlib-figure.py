import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)

y1 = 2*x + 1     # 一元一次方程式

y2 = x**2        # 一元二次方程式

plt.figure()     # figure1
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5))  # 將figure的number設為3  (寬=8,長=5)
plt.plot(x,y2)
plt.plot(x,y1, color="red", linewidth=1.0, linestyle="--")  # 將y1線段放進figure3裡面,設定為線寬1.0的紅色虛線

plt.show()