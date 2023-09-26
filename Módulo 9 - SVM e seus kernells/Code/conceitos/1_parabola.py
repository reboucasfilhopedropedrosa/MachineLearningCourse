import matplotlib.pyplot as plt
import numpy as np
import time

def function(x):
    return x ** 2

def gradient(x):
    return 2 * x


x = 10
learning_rate = 0.1
iterations = 50

x_values = np.linspace(-10, 10, 400)
y_values = function(x_values)
plt.ion()
fig, ax = plt.subplots()
ax.plot(x_values, y_values, label='f(x)=x^2')
point, = ax.plot([], [], 'ro', label='Ponto Atual')

ax.legend()

for i in range(iterations):
    grad = gradient(x)
    y = function(x)
    tangent_line_x = np.array([x - 2, x + 2])
    tangent_line_y = y + grad * (tangent_line_x - x)

    tangent_line, = ax.plot(tangent_line_x, tangent_line_y, 'r--')

    grad = gradient(x)

    x_new = x - learning_rate * grad
    y_new = function(x_new)

    point.set_data(x, y)

    #
    ax.arrow(x, y_new, x_new - x, 0, head_width=0.2, head_length=0.1, fc='purple', ec='purple')  # dx
    ax.arrow(x, y, 0, y_new - y, head_width=0.2, head_length=0.1, fc='green', ec='green')  # dy

    ax.set_title(f"Iteração {i + 1}: x = {x_new:.2f}, f(x) = {y_new:.2f}")

    x = x_new

    plt.pause(3.5)

    tangent_line.remove()

plt.ioff()
plt.show()
