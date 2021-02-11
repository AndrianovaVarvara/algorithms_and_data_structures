import turtle
turtle.shape('turtle')


def doble_circle(a):
    for i in range (36):
        turtle.forward(a)
        turtle.left(10)    
    for i in range (36):
        turtle.forward(a)
        turtle.right(10) 
            
    
turtle.speed(100)
turtle.left(90)

a = 3

for i in range (6):
    doble_circle(a)
    a += 2
    
input ()