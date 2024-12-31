from vpython import sphere, color, vector, rate, curve
import numpy as np

# Parámetros de la simulación
dt = 0.01  # Intervalo de tiempo para cada paso de la simulación
t_max = 20  # Tiempo total de la simulación

# Crear el objeto central (el más grande) en el centro
central_sphere = sphere(pos=vector(0,0,0), radius=105, color=color.yellow)  # Radio en cm

# Crear esferas con diferentes radios
radius1 = 3  # Radio en cm (más pequeño)
radius2 = 45  # Radio en cm (mediano)

# Crear trayectorias elípticas
def elliptical_orbit(a, b, t):
    theta = 2 * np.pi * t / 10  # Periodo de la órbita
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    return vector(x, y, 0)

# Parámetros de las órbitas elípticas
a1, b1 = 150, 150 * 1.5  # Órbita de la esfera mediana (separada)
a2, b2 = 250, 250 * 1.5  # Órbita de la esfera más pequeña (más separada)

# Crear las esferas que orbitan alrededor del objeto central
medium_sphere = sphere(pos=elliptical_orbit(a1, b1, 0), radius=radius2, color=color.blue)
small_sphere = sphere(pos=elliptical_orbit(a2, b2, 0), radius=radius1, color=color.red)

# Crear trayectorias
medium_trajectory = curve(color=color.blue)
small_trajectory = curve(color=color.red)

# Simulación
t = 0
while t < t_max:
    rate(50)  # Controla la velocidad de la animación
    
    # Actualizar las posiciones de las esferas
    medium_sphere.pos = elliptical_orbit(a1, b1, t)
    small_sphere.pos = elliptical_orbit(a2, b2, t)
    
    # Actualizar las trayectorias
    medium_trajectory.append(pos=medium_sphere.pos)
    small_trajectory.append(pos=small_sphere.pos)
    
    t += dt
