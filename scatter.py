from matplotlib import pyplot as plt
x = [2, 3, 4, 5, 6, 7, 9]
y = [6, 7, 8, 9, 3, 4]
colors = 'k'

plt.scatter(x, y, color=colors)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Values'])
plt.show()
