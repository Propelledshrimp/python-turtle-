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

all_turtles = [veronica, hailey]

stalker_turtles = True

veronica.penup() 
veronica.goto(-200,0)
hailey.penup() 
hailey.goto(-200, 50)

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

while True:
    hailey.penup()
    veronica.penup()
    h = hailey.towards(tatem)
    hailey.setheading(h)
    d = veronica.towards(tatem)
    veronica.setheading(d)
    hailey.fd(10)
    veronica.fd(10) 

for t in all_turtles:
    if veronica.position and hailey.position == tatem.position:
        stalker_turtles = False
    while False:
        draw_star(veronica, tatem.x + 100, tatem.y +200, 'red', 'blue') 
        
