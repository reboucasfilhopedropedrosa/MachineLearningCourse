import numpy as np
import matplotlib.pyplot as plt

# Gerar dados
x = np.linspace(-10, 10, 100)
y1 = x**2 + 3      # Parábola aberta para cima
y2 = -(x**2) - 1  # Parábola aberta para baixo

# Plotar pontos originais
plt.figure()
plt.scatter(x, y1, c='r', label='Classe 1')
plt.scatter(x, y2, c='b', label='Classe 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Dados Originais')
plt.legend()
plt.show()



# Transformação polinomial (exemplo simples: elevar ao quadrado)
x1_poly = x**2
y1_poly = y1**2
x2_poly = x**2 + 100
y2_poly = y2**2 + 100

# Plotar pontos transformados
plt.figure()
plt.scatter(x1_poly, y1_poly, c='r', label='Classe 1 transformada')
plt.scatter(x2_poly, y2_poly, c='b', label='Classe 2 transformada')
plt.xlabel('X Transformado')
plt.ylabel('Y Transformado')
plt.title('Dados Transformados')
plt.legend()
plt.show()