import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

theta = np.random.randn(2, 1)
lr = 0.1
iterations = 50


X_b = np.c_[np.ones((100, 1)), X]

theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-10, 10, 100)
Theta0, Theta1 = np.meshgrid(theta0_vals, theta1_vals)
cost_vals = np.zeros((100, 100))

for i in range(100):
    for j in range(100):
        t = np.array([Theta0[i, j], Theta1[i, j]]).reshape(-1, 1)
        cost_vals[i, j] = np.mean((X_b.dot(t) - y) ** 2)

plt.ion()
fig = plt.figure(figsize=(12, 5))


ax1 = fig.add_subplot(121, projection='3d')
ax1.set_xlabel("Theta0")
ax1.set_ylabel("Theta1")
ax1.set_title("Função de Custo")

ax2 = fig.add_subplot(122)
ax2.set_xlabel("X")
ax2.set_ylabel("y")
ax2.set_title("Regressão Linear")

theta_history = []

for iteration in range(iterations):
    gradients = 2 / X_b.shape[0] * X_b.T.dot(X_b.dot(theta) - y)
    theta -= lr * gradients
    theta_history.append(theta.copy())

    ax1.cla()
    ax1.view_init(45, 45)
    ax1.plot_surface(Theta0, Theta1, cost_vals, alpha=0.5, cmap='viridis')

    thetas = np.array(theta_history).reshape(-1, 2)
    ax1.scatter(thetas[:, 0], thetas[:, 1], np.mean((X_b.dot(thetas.T) - y) ** 2, axis=0), color='r')

    ax2.cla()
    ax2.scatter(X, y, alpha=0.7)
    ax2.plot(X, X_b.dot(theta), 'r-', lw=2)

    plt.pause(0.05)

plt.ioff()
plt.show()
