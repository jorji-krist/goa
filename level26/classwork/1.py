from turtle import *

def walk():
    forward(200)
    left(90)

def fall_back():
    left(90)
    forward(200)
    left(180)

walk()
fall_back()

penup()

def both():
    goto(0, 50)
    pendown()
    forward(200)
    left(90)
    left(90)
    forward(200)
    left(180)
both()

exitonclick()