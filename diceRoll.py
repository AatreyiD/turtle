import turtle
import random

dice = [1, 2, 3, 4, 5, 6]
x = 10000
colors = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']

tort = turtle.Turtle()
tort.screen.bgcolor('black')
tort.screen.tracer(1000,5)
tort.pensize(4)
#tort.speed(5)

#tart = turtle.Turtle()

for i in range(x):
    out = random.choice(dice)
    index = i%6
    tort.pencolor(colors[index])
    tort.left(out*60)
    tort.fd(20)

#tort.screen.update()
