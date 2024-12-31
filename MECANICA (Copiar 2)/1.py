from vpython import vector, color, rate, pi, label, curve, sphere, arrow, cos, sin, cylinder, scene
import numpy as np

# Función para calcular la velocidad angular
def calcular_velocidad_angular(periodo):
    return (2 * pi) / periodo  # Velocidad angular = 2π / periodo (en rad/s)

# Parámetros de entrada del usuario
radio = float(input("Ingresa el radio del círculo (en metros): "))  # Radio del círculo
periodo = float(input("Ingresa el período de rotación (en segundos, menor a 1 para más velocidad): "))  # Período de rotación

# Calculamos la velocidad angular
omega = calcular_velocidad_angular(periodo)

# Configuraciones de la escena
scene.background = color.black

# Sistema de referencia (ejes coordenados en el plano cartesiano)
eje_x = curve(pos=[vector(-2*radio, 0, 0), vector(2*radio, 0, 0)], color=color.red, radius=0.01*radio)  # Eje X
eje_y = curve(pos=[vector(0, -2*radio, 0), vector(0, 2*radio, 0)], color=color.green, radius=0.01*radio)  # Eje Y

# Dibujo del círculo usando puntos conectados por líneas
puntos_circulo = 100  # Cantidad de puntos para dibujar el círculo
circulo = curve(color=color.white, radius=0.005*radio)
for i in range(puntos_circulo + 1):
    angulo = 2 * pi * i / puntos_circulo
    x = radio * cos(angulo)
    y = radio * sin(angulo)
    circulo.append(vector(x, y, 0))  # Añadimos los puntos del círculo

# Círculo relleno para mejor visualización
relleno = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 0), radius=radio, color=color.blue, opacity=0.1)

# Etiqueta para mostrar la velocidad angular en pantalla
etiqueta = label(pos=vector(0, 1.5*radio, 0), text=f'Velocidad angular: {omega:.2e} rad/s', height=16, box=False)

# Círculo que rota (punto en el perímetro del círculo)
punto = sphere(pos=vector(radio, 0, 0), radius=0.05*radio, color=color.cyan)

# Flecha que indica la velocidad tangencial
flecha_velocidad = arrow(pos=punto.pos, axis=vector(0.5*radio, 0, 0), color=color.yellow, shaftwidth=0.02*radio)

# Tiempo de simulación
dt = 0.005  # Incremento de tiempo más pequeño para una mayor fluidez

# Animación de la rotación del círculo en el plano cartesiano
angulo = 0  # Ángulo inicial de rotación

# Crear el objeto central sol
central_sphere = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.yellow)

# Crear esferas planetas
radius1 = 0.02  # Radio en metros (pequeño)
radius2 = 0.03  # Radio en metros (mediano)

# Parámetros de las órbitas elípticas
a1, e1 = 0.5, 0.2  # Órbita de la esfera mediana
a2, e2 = 0.7, 0.1  # Órbita de la esfera pequeña

# Velocidades angulares iniciales (relacionadas con el semieje mayor de cada órbita)
speed1 = np.sqrt(1 / a1**3)
speed2 = np.sqrt(1 / a2**3)

# Crear las esferas que orbitan alrededor del Sol
medium_sphere = sphere(pos=vector(a1, 0, 0), radius=radius2, color=color.blue)
small_sphere = sphere(pos=vector(a2, 0, 0), radius=radius1, color=color.red)

# Crear trayectorias
medium_trajectory = curve(color=color.blue)
small_trajectory = curve(color=color.red)

# Ángulos iniciales de las órbitas
theta1, theta2 = 0, 0

# Simulación sin detenerse
while True:
    rate(100)  # Aumentar la velocidad de la animación
    
    # Actualizamos la posición del punto en el círculo usando coordenadas polares
    punto.pos = vector(radio * cos(angulo), radio * sin(angulo), 0)
    
    # Actualizamos la flecha de velocidad tangencial
    flecha_velocidad.pos = punto.pos
    flecha_velocidad.axis = vector(0.5*radio * cos(angulo + pi/2), 0.5*radio * sin(angulo + pi/2), 0)  # Ajusta la dirección a tangente

    # Actualizar las posiciones de las esferas con velocidades angulares diferentes
    medium_sphere.pos = vector(a1 * cos(theta1), a1 * sin(theta1), 0)
    small_sphere.pos = vector(a2 * cos(theta2), a2 * sin(theta2), 0)

    # Actualizar las trayectorias
    medium_trajectory.append(pos=medium_sphere.pos)
    small_trajectory.append(pos=small_sphere.pos)

    # Incrementar ángulo con un factor para hacer que las órbitas sean más rápidas
    theta1 += speed1 * dt
    theta2 += speed2 * dt

    # Actualizamos la etiqueta con la velocidad angular
    etiqueta.text = f'Velocidad angular: {omega:.2e} rad/s\nÁngulo: {angulo:.2f} rad'
    
    # Actualizar el ángulo del círculo
    angulo += omega * dt

