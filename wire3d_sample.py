import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
plt.style.use('_mpl-gallery')

X, Y, Z = axes3d.get_test_data(0.05)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X,Y,Z, rstride=10, cstride=10)
ax.set(xticklabels=[],
yticklabels=[],
zticklabels=[])
plt.show()