#This is a test of the Turtle graphics feature
import math
import random
from turtle import *
tatem = Turtle()
veronica = Turtle()
hailey = Turtle()
tatem.shape("turtle")
veronica.shape("turtle")
hailey.shape("turtle")
all_turtles = [tatem, veronica, hailey]

    
def draw_star(t, x, y, points, line, fill):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.speed(20) 
    turn = 180 - (360 / points) 

    t.color(line, fill)

    t.begin_fill()
    for i in range(points):
        t.forward(200)
        t.left(turn)
    t.end_fill()




draw_star(tatem, 0, 0, 36, "red" , "blue")
draw_star(tatem,200, 200, 36, "green", "yellow")
draw_star(tatem, -200, -200, 36, "orange" , "purple")

draw_star(veronica,-200, 200, 36, "red" , "blue")
draw_star(veronica,200, -200, 36, "green" , "yellow")
draw_star(veronica,100, 100, 36, "green", "yellow")

draw_star(hailey,-100, -100, 36, "orange" , "purple")
draw_star(hailey,-100, 100, 36, "red" , "blue")
draw_star(hailey, 100, -100, 36, "green" , "yellow")
      
for t in all_turtles:
    while True:
        tatem.speed(5)
        veronica.speed(5)
        hailey.speed(5) 
        tatem.fd(random.randint(1, 100))
        veronica.fd(random.randint(1, 100))
        hailey.fd(random.randint(1, 100))
        tatem.right(random.randint(1, 45))
        veronica.right(random.randint(1, 45))
        hailey.right(random.randint(1, 45))
        tatem.left(random.randint(1, 180))
        veronica.left(random.randint(1, 180))
        hailey.left(random.randint(1, 180))

      
       
    
