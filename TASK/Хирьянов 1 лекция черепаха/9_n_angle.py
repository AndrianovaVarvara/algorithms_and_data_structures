import turtle
import math
turtle.shape ('turtle')

n=3
r=10
def more_agles(n, m):  # опеределяем функцию, рисующую многоугольник
    q = 360 / n
    while n > 0:
        turtle.left(q) # угол на который поворачивает черепашка
        turtle.forward(m) # длина стороны
        n -= 1
while n < 13:
    m = 2 * r * math.sin(math.pi / n)  # считаем размер стороны многоугольника (a=2Rsin (360/2n))
    x = (180 - 360 / n) / 2
    turtle.left(x)

    more_agles(n, m)
    turtle.right(x)
    turtle.penup()
    turtle.forward(10)  # задаем расстояние м/у окружностями

    turtle.pendown()
    n += 1
    r += 10

# turtle.shape('turtle')  #черепашка
#
# turtle.left(90/ 3)         #разворачиваем на 30° влево, угол нужно вычислить
# for i in range(3):      #рисуем треугольник как в задании
#     turtle.left(120)
#     turtle.forward(50)
# turtle.right(90 / 3)
#
# turtle.penup()          #поднимаем карандаш
# turtle.forward(30)      #перемещаем карандаш на нужное место
# turtle.pendown()        #опускаем карандаш
#
# turtle.left(180 / 4)
# for n in range (4, 6):
#     R = 55
#     angel = 360 / n
#     dlina = 2 * R * math.sin(180 / n)
#     for i in range(n):
#         turtle.left(angel)
#         turtle.forward(dlina)
#     turtle.right(180 - 360 / n)
#
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
#     R += 5
#     turtle.left(180 - 360 / n)



# n = 3
# R = 50 # мы задаем радиус
# a =  2 * R * math.sin(180 / n) # исходя из него узнаем длину стороны
# angle = 360 / n # внутренний?? угол многоугольника
#
# turtle.speed (1)
# turtle.penup()                 # от серидины надо отступить на R
# turtle.backward(R)
# turtle.left (180 - angle)      # повернем, потому что так в задании
# turtle.pendown()
#
# while n < 5:
#     for i in range (n):
#         turtle.backward (a)             # нарисуем треугольник, она почему то идет задом???
#         turtle.left (angle)
# #turtle.right (180 - angle)       # и теперь поворачиваем обратно, чтобы продолжить наш радиус
#     turtle.penup()
#     turtle.backward(10)               # то на сколько увеличивается наш радиус каждый раз
#     turtle.pendown()
#     n+=1
#
#
#
input ()