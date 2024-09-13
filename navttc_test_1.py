import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
y = np.array([100, 150, 250, 300, 400, 450, 600, 800, 1000, 1500, 1431.5])

mean_x = np.mean(x)
mean_y = np.mean(y)

deviation_x = x - mean_x
deviation_y = y - mean_y

dev = deviation_x * deviation_y

sum_dev = np.sum(dev)

m = sum_dev / np.sum(deviation_x**2)
b = mean_y - (m * mean_x)

def predict(x):
    return m * x + b

# print(predict(12))

plt.plot(x, y)

plt.show()
