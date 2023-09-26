import numpy as np
import matplotlib.pyplot as plt

# Gere pontos 2D em círculos concêntricos
theta = np.linspace(0, 2 * np.pi, 100)
r1 = 3
r2 = 6
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)
x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)

# Plotar pontos originais
plt.figure()
plt.scatter(x1, y1, c='r', label='Classe 1')
plt.scatter(x2, y2, c='b', label='Classe 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Dados Originais')
plt.legend()
plt.show()

# Função RBF
def rbf(x, y, center, gamma=1.0):
    return np.exp(-gamma * np.sum((np.array([x, y]) - center)**2))

# Centro da transformada RBF
center = np.array([0.0, 0.0])

# Aplicar transformada RBF
phi_1 = np.array([rbf(x, y, center) for x, y in zip(x1, y1)])
phi_2 = np.array([rbf(x, y, center) for x, y in zip(x2, y2)])

# Plotar pontos transformados
plt.figure()
plt.scatter(phi_1, np.zeros_like(phi_1), c='r', label='Classe 1 transformada')
plt.scatter(phi_2, np.zeros_like(phi_2), c='b', label='Classe 2 transformada')
plt.xlabel('Transformada RBF')
plt.title('Dados Transformados')
plt.legend()
plt.show()


import time
# Juntar as duas classes transformadas para o algoritmo, mas mantê-las separadas para o plot
x_combined = np.concatenate((phi_1, phi_2))
y_combined = np.concatenate((np.ones_like(phi_1), np.zeros_like(phi_2)))

m = 0
b = 0

alpha = 0.01

n_iterations = 100

n = len(x_combined)

plt.ion()
fig, ax = plt.subplots()

for i in range(n_iterations):

    y_pred = m * x_combined + b
    mse = np.mean((y_combined - y_pred) ** 2)

    dm = - (2 / n) * np.sum((y_combined - y_pred) * x_combined)
    db = -  (2 / n) * np.sum(y_combined - y_pred)

    m = m - alpha * dm
    b = b - alpha * db

    ax.clear()
    ax.scatter(phi_1, np.ones_like(phi_1), c='r', label='Classe 1 real')
    ax.scatter(phi_2, np.zeros_like(phi_2), c='b', label='Classe 2 real')
    ax.plot(x_combined, y_pred, label='Linha ajustada', color='green')
    ax.legend()
    plt.title(f"Iteração {i + 1}, MSE: {mse:.4f}")
    plt.draw()
    plt.pause(0.1)

plt.ioff()
plt.show()
