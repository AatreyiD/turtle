import turtle
def main():
    bitch=turtle.Turtle()
    bitch.pensize(10)

    for i in range(250):                #animate
        bitch.clear()                   #clear screen
        ConcentricCircles(bitch)
        bitch.left(5)                   #turn your turtle a little
        turtle.update()

    turtle.update()                     #show midway product
    turtle.done()

turtle.tracer(0,0)                      #turn off animation

def DrawCircle(T,r):                    
    T.penup()                           #moving to make centre of circle the centre of the page
    T.forward(r)
    T.left(90)
    T.pendown()

    T.color("red")                      #drawing the circle with 3 colours
    T.circle(r,120)
    T.color("green")
    T.circle(r,120)
    T.color("blue")
    T.circle(r,120)

    T.penup()                           #moving back to centre of the page
    T.right(90)
    T.backward(r)

def ConcentricCircles(T):
    for x in range(100,201,20):         #for x in range(lower,upper,step)
        DrawCircle(T,x)
    #100,120,160,220,300

main()
turtle.done()
