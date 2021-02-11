import turtle


def curve_minkovskogo(size, n):
    if n == 0:
        turtle.forward(size)
        return
    curve_minkovskogo(size / 4, n - 1)
    turtle.left(90)
    curve_minkovskogo(size / 4, n - 1)
    turtle.right(90)
    curve_minkovskogo(size / 4, n - 1)
    turtle.right(90)
    curve_minkovskogo(size / 4, n - 1)
    curve_minkovskogo(size / 4, n - 1)
    turtle.left(90)
    curve_minkovskogo(size / 4, n - 1)
    turtle.left(90)
    curve_minkovskogo(size / 4, n - 1)
    turtle.right(90)
    curve_minkovskogo(size / 4, n - 1)


turtle.penup()
turtle.backward(300)
turtle.pendown()

curve_minkovskogo(200, 3)

input()
