import turtle
turtle.shape('turtle')

c = 1
x = 10
while c <= 10:
    for i in range (4):
        turtle.forward(x)
        turtle.left(90)
    turtle.penup()
    turtle.backward (10)
    turtle.penup()
    turtle.right (90)
    turtle.forward (10)
    turtle.left (90)
    turtle.pendown()
    x = x + 20
    c += 1


input() 
    

