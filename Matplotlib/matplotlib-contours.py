import matplotlib.pyplot as plt
import numpy as np

def f(x,y):   # the height function
    return (1-x/2 + x**5 + y**3) * np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

# use plt.contourf to filling contours
# X,Y and value for (X,Y) point

plt.contourf(X, Y, f(X,Y), 8, alpha=0.75, cmap=plt.cm.hot)  # cmap: color map

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X,Y), 8, colors="black", linewidths=0.5)  # 8的意思是將等高線圖 分割成10個部分


# adding label
plt.clabel(C, inline=True, fontsize=10)  # clabel: contour label

plt.xticks(())
plt.yticks(())

plt.show()
