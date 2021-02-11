import turtle
def koch_line(size, n):
    if n == 0:
        turtle.forward(size)
        return
    a = size/3
    koch_line(a, n - 1)
    turtle.left(60)
    koch_line(a, n - 1)
    turtle.right(120)
    koch_line(a, n - 1)
    turtle.left(60)
    koch_line(a, n - 1)

def koch_tri(size, n):
    for i in range(3):
        koch_line(size, n)
        turtle.right(120)

turtle.penup()
turtle.backward(300)
turtle.pendown()
koch_tri (200, 4)

input()
