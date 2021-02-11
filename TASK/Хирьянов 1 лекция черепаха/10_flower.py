import turtle
turtle.shape('turtle')


def circle(a):
    for i in range (36):
        turtle.forward(a)
        turtle.left(10)  
    for i in range (36):
        turtle.forward(a)
        turtle.right(10)         

turtle.speed(10)

a = 10

for i in range (3):
    circle(a)
    turtle.left(60)
    
input ()
