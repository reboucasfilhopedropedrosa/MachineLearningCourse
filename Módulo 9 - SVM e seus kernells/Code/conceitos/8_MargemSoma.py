import numpy as np
import matplotlib.pyplot as plt
import time


def nearest_point_on_line(x0, y0, m, b):

    m1 = -(1 / m)
    b1 =  -(m1 * x0) + y0
    x2 = (b1 - b) / (m-m1)
    y2 = x2*m + b

    return x2, y2


x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([1, 3, 2, 3, 5])


x2 = x1 + 10
y2 = y1 + 10

x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])

m = -4.1
b =  12.1

alpha = 0.9

n_iterations = 100

n = len(x)

plt.ion()
fig, ax = plt.subplots()

for i in range(n_iterations):

    rand_index1 = np.random.choice(len(x1))

    d1 = abs(m * x1  - y1  + b - 1) / np.sqrt(m ** 2 + 1)
    d2 = abs(m * x2  - y2  + b +1) / np.sqrt(m ** 2 + 1)

    mse = np.mean((d1 - d2) ** 2)


    dm = (2 / n) * np.sum((d1 - d2) * (x1  / np.sqrt(x1  ** 2) - x2 / np.sqrt(x2  ** 2)))
    db = (2 / n) * np.sum((d1 - d2) * (1 / np.sqrt(x1  ** 2) - 1 / np.sqrt(x2  ** 2)))

    m = m - alpha * dm
    b = b - alpha * db

    y_pred = m * x + b

    ax.clear()

    plt.axis('equal')
    ax.scatter(x1, y1, label='Dados reais grupo 1')
    ax.scatter(x2, y2, label='Dados reais grupo 2')
    ax.plot(  x , y_pred, label='HiperPlano', color='red')

    ax.plot(x, y_pred+1, label='Margem 1',  linestyle='--' ,color='blue')

    ax.plot(x, y_pred-1, label='Margem 2', linestyle='--', color='blue')

    for j, (xi, yi) in enumerate(zip([x1[rand_index1], x2[rand_index1]], [y1[rand_index1], y2[rand_index1]])):
        if j == 0:
            x_nearest, y_nearest = nearest_point_on_line(xi, yi, m, b-1)
        else:
            x_nearest, y_nearest = nearest_point_on_line(xi, yi, m, b+1)

        ax.plot([xi, x_nearest], [yi, y_nearest], linestyle='--', color='green')

    ax.legend()
    plt.title(f"Iteração {i + 1}, MSE: {mse:.4f}")
    plt.draw()
    plt.pause(0.1)


for x in x1:
    y_pred = m * x + b
    print(y_pred , x)

print(" x2 ")
for x in x2:
    y_pred = m * x + b
    print(y_pred , x)


plt.ioff()
plt.show()
