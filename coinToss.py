import turtle
import random

coin = ['H', 'T']
tort = turtle.Turtle()
x = 100
colors = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']

for i in range(x):
    out = random.choice(coin)
    index = i%6
    if out == 'H':
        tort.pencolor(colors[index])
        tort.left(90)
        tort.fd(10)
    else:
        tort.pencolor(colors[index])
        tort.rt(90)
        tort.fd(10)
