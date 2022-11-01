from matplotlib import pyplot as plt


x = [1, 2, 3, 4, 5]
dev_y = [0, 10, 15, 17.5, 18.75]
dev2_y = [5, 6, 7, 8, 9]

plt.plot(x, dev_y, label='First Deviation')
plt.plot(x, dev2_y, label='Second Deviation')
plt.title("Test Graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()

plt.show()