import matplotlib.pyplot as plt
import numpy as np
import math

# Datos
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
x = []
y = []
for i in range(100):
    x.append(i/10)
    y.append(math.sin(x[i]))

# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('sin(X)')

# Mostrar la gráfica
plt.show()