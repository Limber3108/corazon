import turtle
import time
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Corazón Giratorio con Cambio de Color")
wn.bgcolor("white")  # Fondo blanco
wn.setup(width=400, height=400)

# Función para dibujar un corazón
def draw_heart(color):
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()

# Crear una tortuga
t = turtle.Turtle()
t.shape("circle")
t.speed(3)  # Velocidad más rápida

# Lista de colores para cambiar
colors = ["red", "blue", "green", "purple", "orange", "yellow", "pink", "brown"]

# Hacer que el corazón gire 360 grados y cambie de color cada 2 segundos
angle = 0
while angle < 360:
    t.clear()  # Limpiar el corazón anterior
    color = random.choice(colors)  # Elegir un color aleatorio
    draw_heart(color)  # Dibujar el corazón con el color elegido
    wn.update()  # Actualizar la ventana
    time.sleep(2)  # Esperar 2 segundos
    angle += 5  # Incrementar el ángulo
    t.left(4)  # Girar 5 grados a la izquierda
