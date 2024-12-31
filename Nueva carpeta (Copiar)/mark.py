import matplotlib.pyplot as plt
import numpy as np

# Crear un array de ejemplo
mi_array = np.array([1, 2, 3, 4, 5])

# Graficar
plt.plot(mi_array, marker='o', linestyle='-', color='b', label='Array NumPy')
plt.title('Gráfico del Array de NumPy')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()

# Guardar el gráfico como archivo PNG
plt.savefig('grafico_array.png')  # Guarda el gráfico en el archivo grafico_array.png

# Mostrar el gráfico en pantalla
    
print(mi_array)