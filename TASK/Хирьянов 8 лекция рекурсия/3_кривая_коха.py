import turtle

def koch_line(size, n):
    '''Функция koch_line(size, n) рисует на отрезке длины size кривую Коха
    и делает n итераций (рисует кривую Коха глубины n)'''
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


turtle.penup()
turtle.backward(300)
turtle.pendown()

koch_line(900,3)

input()
