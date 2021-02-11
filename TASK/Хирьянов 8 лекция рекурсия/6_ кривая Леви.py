import turtle

def curve_levi(size, n):
    if n == 0:
        turtle.forward(size)
        return
    turtle.left(45)
    curve_levi(size / 2, n - 1)
    turtle.right(90)
    curve_levi(size / 2, n - 1)
    turtle.left(45)


curve_levi (800,8)
input()
