from vpython import *

# Configuración de la escena
scene.title = "Simulación de velocidad centrípeta y centrífuga"
scene.background = color.black

# Parámetros
radius = 5      # Radio del movimiento circular
omega = 1       # Velocidad angular en rad/s
mass = 1        # Masa del objeto

# Crear el objeto que girará
ball = sphere(pos=vector(radius, 0, 0), radius=0.5, color=color.red)
ball.mass = mass

# Crear el centro de la órbita
center = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.yellow)

# Bucle de simulación
while True:
    rate(100)  # Controla la velocidad de la simulación
    # Calcular la posición del objeto
    ball.pos = vector(radius * cos(omega * scene.time), radius * sin(omega * scene.time), 0)
    
    # Calcular la velocidad centrípeta
    v_c = radius * omega  # Velocidad centrípeta
    # Calcular la fuerza centrípeta
    f_c = mass * (v_c**2) / radius  # Fuerza centrípeta
    # Mostrar la velocidad centrípeta y fuerza centrípeta
    label(pos=ball.pos + vector(0, 1, 0), text=f"v_c: {v_c:.2f}, f_c: {f_c:.2f}", color=color.white)


