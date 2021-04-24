import matplotlib.pyplot as plt
import numpy as np

n = 1024

x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)

color = np.arctan2(y,x)  # for color value

plt.scatter(x, y, s=75, c=color, alpha=0.5)
# plt.scatter(np.arange(5), np.arange(5))

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

plt.xticks(())
plt.yticks(())

plt.show()