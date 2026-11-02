import matplotlib.pyplot as plt

# Datos
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Crear la gráfica de barras
plt.barh(categorias, valores, color=['red', 'blue', 'green', 'orange'])

# Agregar título y etiquetas
plt.title('Gráfica de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar la gráfica
plt.show()