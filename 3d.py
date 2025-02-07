import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[3,6,10,15],'p-')
plt.plot([3,4,6,9],'c-')
plt.plot([9,2,3,4],'m-')
plt.bar([5,2,8,9],[8,3,9,10])
plt.axis([0,6,0,20])
plt.ylabel('some numbers')
plt.show()