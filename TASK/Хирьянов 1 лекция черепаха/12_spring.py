import turtle
turtle.shape('turtle')
turtle.left(90)

def spr(a):
    for i in range (180):
        turtle.forward(a)
        turtle.right(1)  
    for i in range (180):
            turtle.forward(a/5)
            turtle.right(1) 

turtle.speed(10)
a = 1

for i in range (5):
    spr(a)
    
input ()
