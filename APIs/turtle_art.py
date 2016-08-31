import turtle
window = turtle.Screen()
window.bgcolor("white")

def draw_triangle(noelis):
    for x in range(0, 2):
        noelis.pendown()
        noelis.right(60)
        noelis.forward(30)

def main():
	noelis = turtle.Turtle()

	noelis.shape("classic")
	noelis.color("purple", none)
	noelis.penup()
	noelis.setx(-150)

	noelis.begin_fill()
	draw_triangle(noelis)
	noelis.end_fill()

	window.exitonclick()

if __name__ == '__main__':
	main()