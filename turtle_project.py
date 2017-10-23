from turtle import * 
import math
import random

tatem = Turtle()
veronica = Turtle()
hailey = Turtle()

all_turtles = [ tatem, veronica, hailey]


def draw_star(t, x, y , points, line, fill):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.speed(10)
    turn = (180 - 360 / points)

    t.color(line,fill)

    t.begin_fill()
    for i in range(points):
        t.forward(200)
        t.left(turn)
    t.end_fill()



        

draw_star(tatem, 200, 200, 36 , 'orange' , 'yellow')
 
