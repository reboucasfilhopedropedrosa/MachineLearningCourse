import numpy as np
import matplotlib.pyplot as plt

def update_weights(w, b, X, y, alpha):
    for i in range(len(X)):
        xi, label = X[i], y[i]
        condition = label * (np.dot(w, xi) + b)
        if condition < 1:
            w = w + alpha * ( (xi * label) - (2 * (1/len(X)) * w) )
            b = b + alpha * label
        else:
            w = w - alpha * (2 * (1/len(X)) * w)
    return w, b

np.random.seed(0)
X1 = np.random.randn(20, 2) + np.array([2, 2])
X2 = np.random.randn(20, 2) + np.array([-2, -2])

X = np.vstack([X1, X2])
y = np.hstack([np.ones(20), -1*np.ones(20)])

w = np.random.randn(2)
b = np.random.randn()+1

alpha = 0.01

plt.ion()
fig, ax = plt.subplots()

for i in range(1000):
    w, b = update_weights(w, b, X, y, alpha)

    ax.clear()
    ax.scatter(X1[:, 0], X1[:, 1], label='Classe 1')
    ax.scatter(X2[:, 0], X2[:, 1], label='Classe 2')
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = -(w[0] * xx + b) / w[1]

    plt.plot(xx, yy, 'k-')

    yy = -(w[0] * xx + b + 1) / w[1]
    plt.plot(xx, yy, 'k--')

    yy = -(w[0] * xx + b - 1) / w[1]
    plt.plot(xx, yy, 'k--')

    plt.pause(0.1)

plt.ioff()
plt.show()
