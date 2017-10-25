from turtle import * 
import math
import random  

god = Turtle() 
tatem = Turtle()
veronica = Turtle()
hailey = Turtle()
tatem.shape("turtle")
veronica.shape("turtle")
hailey.shape("turtle") 

all_turtles = [ tatem, veronica, hailey]

green_hill = Screen()
green_hill.screensize(2000,2000)
green_hill.title("Turtle Plains")

green_hill.bgpic() 
green_hill.bgpic("turtle_background.png")


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
    t.hideturtle() 
def up_arrow():
    tatem.penup()
    tatem.fd(100)
def down_arrow():
    tatem.penup() 
    tatem.back(100)
def right_arrow():
    tatem.penup() 
    tatem.right(45)
def left_arrow():
    tatem.penup() 
    tatem.left(45)  
    
onkeypress(up_arrow, "Up")
onkeypress(down_arrow, "Down")
onkeypress(left_arrow, "Left")
onkeypress(right_arrow, "Right")
listen() 
    



        

draw_star(god, 200, 200, 36 , 'orange' , 'yellow')

 
