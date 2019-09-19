from turtle import *

shape("turtle")
pendown()
speed = 0
for j in range(10):
    for i in range(4):
        forward(20 * j + 10)
        left(90)
    penup()
    left(270)
    forward(10)
    left(270)
    forward(10)
    left(180)
    pendown()