import turtle
turtle.speed(50)

# задаем функцию по которой будет рисоваться квадрат с длиной стороны а

def sq(a):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)

# задаем длину стороны, и с каждым новым квадратом увеличиваем на х         

dlina = 10

for i in range(50):
    sq(dlina)
    turtle.right(10)
    dlina +=5
    
input()    