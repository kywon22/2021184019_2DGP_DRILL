import turtle

def up_move():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def down_move():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)

def left_move():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def right_move():
    turtle.stamp()
    turtle.setheading(360)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape("turtle")
turtle.onkey(up_move, 'w')
turtle.onkey(down_move, 's')
turtle.onkey(left_move, 'a')
turtle.onkey(right_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
