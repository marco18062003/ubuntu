from vpython import *

# Solicitar datos al usuario
print("========== hola ==========")
print("Gravedad de refeerncia de diferentes planetas y el sol")
gravedad_planetas = {
    "Mercurio": 3.7,
    "Venus": 8.87,
    "Tierra": 9.81,
    "Marte": 3.71,
    "Júpiter": 24.79,
    "Saturno": 10.44,
    "Urano": 8.69,
    "Neptuno": 11.15
}

gravedad_sol = 274.0

# Imprimir la gravedad de cada planeta y del Sol
for planeta, gravedad in gravedad_planetas.items():
    print(f"La gravedad de {planeta} es {gravedad} m/s^2")
print("==================================")
print(f"La gravedad del Sol es {gravedad_sol} m/s^2")
print("==============================")
velocidad_escape = {
    "Mercurio": 4250,
    "Venus": 10360,
    "Tierra": 11190,
    "Marte": 5030,
    "Júpiter": 59540,
    "Saturno": 35500,
    "Urano": 21300,
    "Neptuno": 23560
}

velocidad_escape_sol = 617700  # Velocidad de escape del Sol en m/s

# Imprimir la velocidad de escape de cada planeta y del Sol
for planeta, velocidad in velocidad_escape.items():
    print(f"La velocidad de escape de {planeta} es {velocidad} m/s")

print(f"La velocidad de escape del Sol es {velocidad_escape_sol} m/s")

print(f"La velocidad de escape del Sol es {velocidad_escape_sol} km/s")
print("============ Datos para ejecutar ==========")
g = float(input("Ingrese la gravedad (m/s^2): "))  # m/s^2
v0 = float(input("Ingrese la velocidad inicial (m/s): "))  # m/s
angle = float(input("Ingrese el ángulo de lanzamiento (grados): "))  # grados

# Convertir ángulo a radianes
angle_rad = radians(angle)

# Componentes de la velocidad inicial
vx = v0 * cos(angle_rad)
vy = v0 * sin(angle_rad)

# Crear el plano cartesiano
grid_size = 50  # Tamaño de la cuadrícula

# Crear el plano
plane = box(pos=vector(grid_size/2, -0.01, 0), size=vector(grid_size, 0.02, grid_size), color=color.gray(0.5), opacity=0.3)

# Crear los ejes cartesianos con líneas más delgadas
x_axis = curve(pos=[vector(0, 0, 0), vector(grid_size, 0, 0)], color=color.red, radius=0.02)  # Eje X desde 0 hasta grid_size
y_axis = curve(pos=[vector(0, 0, 0), vector(0, grid_size, 0)], color=color.green, radius=0.02)  # Eje Y desde 0 hasta grid_size

# Crear marcas en los ejes
def create_ticks(axis, start, end, interval, tick_length=0.3, tick_color=color.black):
    for i in range(start, end + interval, interval):
        # Marca en el eje X
        if axis == 'x':
            tick = box(pos=vector(i, -tick_length, 0), size=vector(0.02, tick_length * 2, 0), color=tick_color)
            label(pos=vector(i, -tick_length * 2, 0), text=str(i), box=False, height=12, color=color.black)
        # Marca en el eje Y
        elif axis == 'y':
            tick = box(pos=vector(-tick_length, i, 0), size=vector(tick_length * 2, 0.02, 0), color=tick_color)
            label(pos=vector(-tick_length * 2, i, 0), text=str(i), box=False, height=12, color=color.black)

# Añadir marcas en los ejes X e Y
create_ticks('x', 0, grid_size, 5)
create_ticks('y', 0, grid_size, 5)

# Crear el proyectil
projectile = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.blue, make_trail=True)

# Crear el misil en la punta del proyectil
missile = cylinder(pos=projectile.pos + vector(0, 0.5, 0), axis=vector(0, 1, 0), radius=0.2, length=1, color=color.red)

# Tiempo
dt = 0.01

# Bucle infinito para repetir el movimiento
while True:
    t = 0  # Reiniciar el tiempo para cada ciclo
    
    # Reiniciar la posición y el rastro del proyectil
    projectile.pos = vector(0, 0, 0)
    missile.pos = projectile.pos + vector(0, 0.5, 0)  # Posicionar el misil en la punta
    missile.axis = vector(0, 1, 0)  # Orientación del misil
    projectile.clear_trail()  # Limpiar el rastro anterior
    
    # SimulaaaaaaaaaOOación del movimiento parabólico
    while projectile.pos.y >= 0:
        rate(100)  # Controla la velocidad de la simulación
        x = vx * t  # Posición en x
        y = vy * t - 0.5 * g * t**2  # Posición en y con el efecto de la gravedad
        projectile.pos = vector(x, y, 0)  # Actualiza la posición del proyectil
        missile.pos = projectile.pos + vector(0, 0.5, 0)  # Actualiza la posición del misil en la punta del proyectil
        t += dt  # Incrementa el tiempo
