import turtle

def turtled_function(start_x, start_y, finish_x, finish_y):
    turtle.speed(1)
    turtle.pencolor("blue")
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(start_x,start_y)
    turtle.pendown()
    turtle.goto(finish_x,  finish_y)
    
turtled_function(230, -145, -155, 170)