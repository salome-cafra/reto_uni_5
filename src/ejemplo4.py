import matplotlib.pyplot as plt

# Datos
etiquetas = ['Manzanas', 'Bananas', 'Cerezas', 'Dátiles']
tamaños = [15, 30, 45, 10]

# Crear la gráfica de pastel
plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)

# Asegurar que el gráfico sea circular
plt.axis('equal')

# Agregar título
plt.title('Distribución de Frutas')

# Mostrar la gráfica
plt.show()