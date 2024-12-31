from vpython import *

# Parámetros
g = 9.8  # m/s^2
v0 = 30  # m/s
angle = 45  # grados

# Convertir ángulo a radianes
angle_rad = radians(angle)

# Componentes de la velocidad inicial
vx = v0 * cos(angle_rad)
vy = v0 * sin(angle_rad)

# Crear el proyectil
projectile = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.blue, make_trail=True)

# Crear los ejes cartesianos
x_axis = curve(pos=[vector(-10, 0, 0), vector(50, 0, 0)], color=color.red)  # Eje X
y_axis = curve(pos=[vector(0, -10, 0), vector(0, 50, 0)], color=color.green)  # Eje Y

# Añadir números al eje X
for i in range(-10, 51, 10):
    label(pos=vector(i, -2, 0), text=str(i), box=False, height=12, color=color.white)

# Añadir números al eje Y
for j in range(0, 51, 10):
    label(pos=vector(-2, j, 0), text=str(j), box=False, height=12, color=color.white)

# Tiempo
t = 0
dt = 0.01

# Simulación del movimiento parabólico
while projectile.pos.y >= 0:
    rate(100)  # Controla la velocidad de la simulación
    x = vx * t  # Posición en x
    y = vy * t - 0.5 * g * t**2  # Posición en y con el efecto de la gravedad
    projectile.pos = vector(x, y, 0)  # Actualiza la posición del proyectil
    t += dt  # Incrementa el tiempo

