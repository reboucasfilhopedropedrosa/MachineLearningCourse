import numpy as np
import matplotlib.pyplot as plt
import time

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 2, 3, 5])

m = 0
b = 0

alpha = 0.01

n_iterations = 100

n = len(x)

plt.ion()
fig, ax = plt.subplots()

for i in range(n_iterations):

    y_pred = m * x + b
    mse = np.mean((y - y_pred) ** 2)

    dm = - (2 / n) * np.sum((y - y_pred) * x)
    db = -  (2 / n) * np.sum(y - y_pred)

    m = m - alpha * dm
    b = b - alpha * db

    ax.clear()
    ax.scatter(x, y, label='Dados reais')
    ax.plot(x, y_pred, label='Linha ajustada', color='red')
    ax.legend()
    plt.title(f"Iteração {i + 1}, RMSE: {mse:.4f}")
    plt.draw()
    plt.pause(3.1)

plt.ioff()
plt.show()
