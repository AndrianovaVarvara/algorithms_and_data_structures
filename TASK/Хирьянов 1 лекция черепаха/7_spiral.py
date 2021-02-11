import turtle
turtle.shape('turtle')

x = 1
a = 10

turtle.forward (x)
turtle.left (a)

for i in range (100):
    turtle.forward (x)
    turtle.left (a)
    x += 0.1
    turtle.forward (x)
    turtle.left (a)
    

input()
