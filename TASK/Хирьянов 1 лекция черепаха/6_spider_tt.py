import turtle
turtle.shape('turtle')

n = 8
angel = 360 / n
x = 100

for n in range (n):
    turtle.right(angel)
    turtle.forward(x)
    turtle.stamp()
    turtle.backward(x)
    
input() 
    

