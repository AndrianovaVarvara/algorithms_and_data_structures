import turtle
turtle.shape('turtle')

x = 11
dlina = 200
angle = 180 - (180 / x)

turtle.penup()
turtle.left(180/x)
turtle.forward(dlina/2)
turtle.pendown()
turtle.bgcolor('black')
turtle.pencolor('yellow')

for i in range(x):
    turtle.left(angle)
    turtle.forward(dlina)

input()