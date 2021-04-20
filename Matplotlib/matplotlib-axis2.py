import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)

y1 = 2*x + 1     # 一元一次方程式

y2 = x**2        # 一元二次方程式

plt.figure(figsize=(9,5))
plt.plot(x,y2)
plt.plot(x,y1, color="red", linewidth=1.0, linestyle="--")

plt.xlim((-1,2))   # x limits (left, right)
plt.ylim((-2,3))   # y limits (bottom, top)

plt.xlabel("(x)")
plt.ylabel("(y)")

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.5, -1, 1.22, 3],[r"$really\ bad$",r"$bad$",r"$normal$",r"$good$",r"$really\ good$"])
                                    # 正則表達式 r = regular 正規的

ax = plt.gca()   # gca = "get current axis"
ax.spines["right"].set_color("none")   # 將右邊和頂部的軸設為透明
ax.spines["top"].set_color("none")

ax.xaxis.set_ticks_position("bottom")  # 將底部的軸設為x軸
ax.yaxis.set_ticks_position("left")    # 將左邊的軸設為y軸

ax.spines["bottom"].set_position(("data", 0))  # 將線段位置設為經過原點(0,0)
ax.spines["left"].set_position(("data", 0))

plt.show()