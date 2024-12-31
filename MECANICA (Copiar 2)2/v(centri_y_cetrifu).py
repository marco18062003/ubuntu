from vpython import *

# Crear el escenario
scene = canvas(title="Simulación Didáctica: Velocidad Centrípeta y Centrífuga")

# Instrucciones iniciales para el usuario
print("Bienvenido a la simulación de velocidad centrípeta y centrífuga.")
print("Por favor, ingrese los siguientes parámetros:")

# Solicitar datos al usuario
radio = float(input("Ingrese el radio del círculo (en unidades, p.ej., metros): "))
velocidad = float(input("Ingrese la velocidad angular (en rad/s): "))
masa = float(input("Ingrese la masa del objeto (en kg): "))

# Crear el objeto que se moverá (una esfera)
objeto = sphere(pos=vector(radio, 0, 0), radius=0.5, color=color.blue, make_trail=True)

# Crear marcadores para las fuerzas
fuerza_centripeta = arrow(pos=objeto.pos, axis=vector(0, 0, 0), color=color.red, shaftwidth=0.1)
fuerza_centrifuga = arrow(pos=objeto.pos, axis=vector(0, 0, 0), color=color.green, shaftwidth=0.1)

# Definir tiempo inicial y paso de tiempo
t = 0
dt = 0.01

# Explicación sobre las fuerzas
print("\nLa fuerza centrípeta (roja) actúa hacia el centro del círculo.")
print("La fuerza centrífuga (verde) es una fuerza ficticia que actúa hacia afuera.")
print("La simulación comenzará ahora.\n")

while True:
    rate(100)  # Controlar la velocidad de la simulación

    # Calcular la nueva posición del objeto en movimiento circular
    x = radio * cos(velocidad * t)
    y = radio * sin(velocidad * t)
    objeto.pos = vector(x, y, 0)

    # Calcular y actualizar la fuerza centrípeta
    fuerza_centripeta.pos = objeto.pos
    fuerza_centripeta.axis = vector(-masa * velocidad**2 / radio * 2, 0, 0)  # Duplicar longitud para mayor visibilidad

    # Calcular y actualizar la fuerza centrífuga
    fuerza_centrifuga.pos = objeto.pos
    fuerza_centrifuga.axis = vector(masa * velocidad**2 / radio * 2, 0, 0)  # Duplicar longitud para mayor visibilidad

    # Incrementar el tiempo
    t += dt

