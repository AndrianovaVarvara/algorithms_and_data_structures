import turtle

def zzz(size, n, angle=90):

    if n == 0:
        turtle.forward(size)


        return
    zzz(size, n -1)
    turtle.left(angle)
    zzz(size, n - 1)
    turtle.right(angle)
    zzz(size, n - 1)
    turtle.right(angle)
    zzz(size, n - 1)
    turtle.left(angle)
    zzz(size, n - 1)

turtle.penup()
turtle.backward(300)
# turtle.left(90)
# turtle.forward(200)
# turtle.right(90)
turtle.pendown()
zzz(20,2)
