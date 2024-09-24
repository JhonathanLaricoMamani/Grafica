import numpy as np
import matplotlib.pyplot as plt

# Definir los coeficientes
A = np.array([[1.0001, 1.0],
              [1.0, 1.0]])
b = np.array([2, 2])

# Resolver el sistema de ecuaciones
sol = np.linalg.solve(A, b)

# Crear puntos para las líneas
x_vals = np.linspace(-10, 10, 400)
y1_vals = 2 - 1.0001 * x_vals  # Ecuación 1: y = 2 - 1.0001x
y2_vals = 2 - 1 * x_vals       # Ecuación 2: y = 2 - x

# Graficar
plt.plot(x_vals, y1_vals, label='1.0001x + y = 2')
plt.plot(x_vals, y2_vals, label='x + y = 2')

# Mostrar la solución
plt.scatter(sol[0], sol[1], color='red', zorder=5, label=f'Solución: x={sol[0]:.4f}, y={sol[1]:.4f}')

# Etiquetas y leyenda
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.grid(True)
plt.show()
