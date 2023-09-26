import numpy as np
import matplotlib.pyplot as plt
import time

theta = np.linspace(0, 2 * np.pi, 100)
r1 = 3
r2 = 6
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)
x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)


m = 0.1
b = 0.1
alpha = 0.01
n_iterations = 100
n = len(x1)

plt.ion()
plt.axis('equal')

fig, ax = plt.subplots()

ax.clear()
plt.axis('equal')

ax.scatter(x1, y1, label='Grupo 1')
ax.scatter(x2, y2, label='Grupo 2')

plt.draw()
plt.pause(0.1)

plt.ioff()
plt.show()
