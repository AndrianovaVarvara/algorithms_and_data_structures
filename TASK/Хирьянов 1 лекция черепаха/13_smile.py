import turtle
turtle.shape('turtle')

# face
turtle.color('yellow')
turtle.begin_fill()
for i in range (36):
        turtle.forward(15)
        turtle.left(10)  
turtle.end_fill()

# eyes

a = 2
left = -30
right = 30

turtle.color('blue')
turtle.begin_fill()
turtle.penup()
turtle.setposition(left,100)
turtle.pendown()
for i in range (36):
    turtle.forward(a)
    turtle.left(10)  
turtle.end_fill()  
    
turtle.penup()
turtle.setposition(right,100)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
for i in range (36):
    turtle.forward(a)
    turtle.left(10) 
turtle.end_fill()   

turtle.penup()
turtle.setposition(0,80)
turtle.pendown()

# nose

turtle.pencolor('black')
turtle.pensize(5)
turtle.right(90)
turtle.forward(20)
turtle.left(90)

turtle.penup()
turtle.setposition(40,60)
turtle.pendown()

# mought

turtle.right(90)
turtle.pencolor('red')
for i in range (18):
        turtle.forward(7)
        turtle.right(10)

   
input()