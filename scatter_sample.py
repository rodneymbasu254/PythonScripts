import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
x = plt.axes(projection = "3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

plt.title("Sample 3d")
plt.xlabel("mahn")
plt.ylabel("ziii")


plt.scatter(x, y, z)
plt.show()