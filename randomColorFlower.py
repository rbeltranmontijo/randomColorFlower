from turtle import *
from random import randint


Screen()

speed(0)
bgcolor('black')


for i in range(24):
    for i in range(12):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        pencolor(r, g, b) # en cada movimiento, se genera un color aleatorio
        circle(35, 60)
        right(80)
    right(45)

exitonclick()
