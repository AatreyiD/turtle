import turtle
def main(n,size):
	bit=turtle.Turtle()
	bit.speed(0)
	bit.pensize(3)
	for b in range(n):
		angle=360/n
		DrawPolygon(bit,n,size/2)
		bit.forward(size)
		bit.right(angle)
def DrawPolygon(tortle,n,size):
	angle=360/n
	for a in range(n):
		tortle.forward(size)
		tortle.right(angle)
n = int(input("enter number of sides"))
main(n,100)
turtle.done()
