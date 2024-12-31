from vpython import sphere, color, vector, rate, curve
import numpy as np

# Parámetros de la simulación
dt = 0.01  # Intervalo de tiempo para cada paso de la simulación

# Crear el objeto central (el más grande) en el centro
central_sphere = sphere(pos=vector(0,0,0), radius=105, color=color.yellow)  # Radio en cm

# Crear esferas con diferentes radios
radius1 = 3  # Radio en cm (más pequeño)
radius2 = 45  # Radio en cm (mediano)
radius3 = 10  # Radio de las nuevas esferas (puedes ajustarlo)

# Crear trayectorias elípticas con diferente velocidad
def elliptical_orbit(a, b, t, speed_factor):
    theta = 2 * np.pi * t / (10 * speed_factor)  # Controla la velocidad de la órbita
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    return vector(x, y, 0)

# Parámetros de las órbitas elípticas
a1, b1 = 150, 150 * 1.5  # Órbita de la esfera mediana
a2, b2 = 250, 250 * 1.5  # Órbita de la esfera pequeña
a3, b3 = 350, 350 * 1.5  # Órbita para la nueva esfera 1
a4, b4 = 450, 450 * 1.5  # Órbita para la nueva esfera 2
a5, b5 = 550, 550 * 1.5  # Órbita para la nueva esfera 3

# Velocidades (factores de velocidad)
speed1 = 1  # Velocidad normal
speed2 = 0.8  # Más lenta
speed3 = 1.2  # Más rápida
speed4 = 0.6  # Muy lenta
speed5 = 1.5  # Muy rápida

# Crear las esferas que orbitan alrededor del objeto central
medium_sphere = sphere(pos=elliptical_orbit(a1, b1, 0, speed1), radius=radius2, color=color.blue)
small_sphere = sphere(pos=elliptical_orbit(a2, b2, 0, speed2), radius=radius1, color=color.red)

# Nuevas esferas
sphere1 = sphere(pos=elliptical_orbit(a3, b3, 0, speed3), radius=radius3, color=color.green)
sphere2 = sphere(pos=elliptical_orbit(a4, b4, 0, speed4), radius=radius3, color=color.orange)
sphere3 = sphere(pos=elliptical_orbit(a5, b5, 0, speed5), radius=radius3, color=color.purple)

# Crear trayectorias
medium_trajectory = curve(color=color.blue)
small_trajectory = curve(color=color.red)
trajectory1 = curve(color=color.green)
trajectory2 = curve(color=color.orange)
trajectory3 = curve(color=color.purple)

# Simulación sin detenerse
t = 0
while True:  # Ciclo infinito para que la simulación no se detenga
    rate(50)  # Controla la velocidad de la animación
    
    # Actualizar las posiciones de las esferas con diferentes velocidades
    medium_sphere.pos = elliptical_orbit(a1, b1, t, speed1)
    small_sphere.pos = elliptical_orbit(a2, b2, t, speed2)
    sphere1.pos = elliptical_orbit(a3, b3, t, speed3)
    sphere2.pos = elliptical_orbit(a4, b4, t, speed4)
    sphere3.pos = elliptical_orbit(a5, b5, t, speed5)
    
    # Actualizar las trayectorias
    medium_trajectory.append(pos=medium_sphere.pos)
    small_trajectory.append(pos=small_sphere.pos)
    trajectory1.append(pos=sphere1.pos)
    trajectory2.append(pos=sphere2.pos)
    trajectory3.append(pos=sphere3.pos)
    
    # Incrementar el tiempo
    t += dt
