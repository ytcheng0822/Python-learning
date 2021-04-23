import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)

y1 = 2*x + 1     # 一元一次方程式

y2 = x**2        # 一元二次方程式

plt.figure(figsize=(9,5))


plt.xlim((-1,2))   # x limits (left, right)
plt.ylim((-2,3))   # y limits (bottom, top)

plt.xlabel("(x)")
plt.ylabel("(y)")

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.5, -1, 1.22, 3],[r"$really\ bad$",r"$bad$",r"$normal$",r"$good$",r"$really\ good$"])
                                    # 正則表達式 r = regular 正規的


l1, = plt.plot(x,y2)               # 要放入列表當成物件必須加上 ,         
l2, = plt.plot(x,y1, color="red", linewidth=1.0, linestyle="--")


plt.legend(handles=[l1,l2], labels=["solid line","dashed line"], loc="best")  # solid line實線  dashed line虛線

plt.show()