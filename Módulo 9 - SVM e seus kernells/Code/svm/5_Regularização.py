import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()
fig, ax = plt.subplots()
text = ax.text(0.1, 0.9, '', transform=ax.transAxes)

num_points = 2
num_iterations = 20
range_min = 0
range_max = 1

ax.set_xlim(range_min, range_max)
ax.set_ylim(range_min, range_max)

for i in range(num_iterations):
    ax.clear()

    vector1 = np.random.uniform(range_min, range_max, num_points)
    vector2 = np.random.uniform(0, 1, num_points)
    result = np.dot(vector1, vector2)

    scaled_vector = (vector1 ) * (result )

    ax.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label="Vetor 1")
    ax.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='b', label="Vetor 2")
    ax.quiver(0, 0, scaled_vector[0], scaled_vector[1], angles='xy', scale_units='xy', scale=1, color='g',
              label=f'Produto Escalar como Vetor (Vetor 1 * {result})')

    text = ax.text(0.1, 0.9, f'Produto Escalar: {result}', transform=ax.transAxes)

    ax.set_xlim(range_min, range_max)
    ax.set_ylim(range_min, range_max)
    ax.legend()

    plt.draw()
    plt.pause(1)

plt.ioff()
plt.show()
