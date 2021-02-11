import turtle

x = 10

turtle.forward (x)
turtle.left (90)

for i in range (10):
    turtle.forward (x)
    turtle.left (90)
    x += 10
    turtle.forward (x)
    turtle.left (90)
    

input()
