import turtle

window = turtle.Screen()
window.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# Dibujar el tallo del girasol
t.penup()
t.goto(0, -100)  # Posicionar el comienzo del tallo
t.setheading(270)  
t.pendown()
t.color("green")
t.pensize(10)
t.forward(300)  # Longitud del tallo

# Dibujar una hoja
t.penup()
t.goto(0, -200) 
t.setheading(180)  # Girar hacia la izquierda
t.pendown()
t.begin_fill()
t.circle(50, 90)  # Dibujar la curva de la hoja
t.left(90)
t.circle(50, 90)
t.end_fill()

# Dibujar los pétalos del girasol
t.penup()
t.goto(0, -35)  # Posicionar para los pétalos
t.setheading(0)
t.pendown()
t.pensize(1)

# Función para dibujar un pétalo más grande
def dibujar_petalo():
    t.color("yellow")
    t.begin_fill()
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(120)
    t.end_fill()

# Dibujar los pétalos del girasol
for _ in range(18):
    dibujar_petalo()
    t.right(20)

# Dibujar el centro del girasol
t.penup()
t.goto(0, -75)
t.pendown()
t.color("brown")
t.begin_fill()
t.circle(40)  
t.end_fill()

t.hideturtle()
window.mainloop()
