import turtle
bitch=turtle.Turtle()
def main():
    turtle.tracer(0,0)
    bitch.pensize(1)
    bitch.hideturtle()

    bitch.penup()                   #don't draw line to starting pos
    bitch.setpos(-300,-300)         #start at position (x,y)
    bitch.pendown()

    A,B,C=Triangle(bitch,700)       #call triangle and store vertices

    LotsOfTriangles(bitch,A,B,C,6)  #call LotsOfTriangles function

    turtle.update()         #finish up
    turtle.done()



def Triangle(T,size):  
    V=[]                        #in form V[i]=(x,y)
    for i in range(3):
        V.append(T.pos())       #store vertice position in array
        T.forward(size)         #draw triangle
        T.left(120)             #rotate

    return V                    #V = [(xA,yA), (xB,yB), (xC,yC)]

def midpoint(P,Q):
    midX=(P[0]+Q[0])/2
    midY=(P[1]+Q[1])/2
    return midX, midY

def ReverseTriangle(T,A,B,C):
    midAB=((A[0]+B[0])/2 , (A[1]+B[1])/2)   #calculate midpoints
    midBC=((B[0]+C[0])/2 , (B[1]+C[1])/2)   #A in form [x,y]
    midCA=((C[0]+A[0])/2 , (C[1]+A[1])/2)   #so A[0] = x and A [1] = y
    #print(f"The 3 points are {midAB}, {midBC}, {midCA}")    #f is for formatted staements to avoid using "" everywhere

    T.penup()
    T.setpos(midAB)         #move (without drawing) to one of the midpoints
    T.pendown()

    T.setpos(midBC)         #draw the reversed triangle by teleporting between midpoints
    T.setpos(midCA)
    T.setpos(midAB)

    return midAB, midBC, midCA      #return midpoints

def LotsOfTriangles(T,A,B,C,layers):
    if layers<0:        #if 0 layers left, stop the code
        return

    midAB,midBC,midCA=ReverseTriangle(bitch,A,B,C)      #call reverse triangle to calculate vertices

    LotsOfTriangles(bitch,  A  ,midAB,midCA,layers-1)   #call LotsOfTriangles for each of these new midpoints          #3rd set of triangles
    LotsOfTriangles(bitch,midAB,  B  ,midBC,layers-1)
    LotsOfTriangles(bitch,midCA,midBC,  C  ,layers-1)

main()
