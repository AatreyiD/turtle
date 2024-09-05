import turtle
import random

t0 = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()
t9 = turtle.Turtle()

turtles = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9]
n = len(turtles)

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor('black')

screen.tracer(False)

# initialise turtles
def initTurtle(x,y):
    # m = random.randint(2,n)   # random number of worms between 2 to 10
    sz = 0.05
    # ang = 360/m   # angle isn't working for random number of worms?
    for t in range (n):
        turtles[t].left(360*(t/n))
        turtles[t].hideturtle()
        turtles[t].pensize(sz)
        turtles[t].pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        turtles[t].penup()
        turtles[t].setpos(x,y)
        turtles[t].pendown()
    worm(n)    
        
def worm(n):
    sz = 0.05
    theta = 0.5 # for spiral
    for a in range (80):
        for t in range (n):
            sz+=0.05
            turtles[t].pensize(sz)
            turtles[t].forward(10)
            # theta = 0 # for straight line
            # theta = random.randint(-45,45)    # for worm
            (r,g,b) = turtles[t].pencolor()
            if r<255:
                r = r+1
            if g<254:
                g = g+1
            if b<254:
                b = b+1
            turtles[t].pencolor((int(r),int(g),int(b)))
            turtles[t].left(theta)
        theta += 0.5    # for spiral
        screen.update()

screen.onclick(initTurtle)
