#1
from turtle import *
def window():
    wn = Screen()
    wn.bgcolor("light blue")
    wn.setup(height=1600, width=900)
window()

def walk():
    for i in range(120):
        speed(100)
        color("yellow")
        begin_fill()
        forward(100)
        left(120)
        forward(100)
        left(120)
        forward(100)
        left(30)
        end_fill()
        penup()
        forward(100)
        pendown()
        left(90)
walk()
exitonclick()

#2
def hello_world():
    print("Hello, World!")

a = "hello_world"

if a == "hello_world":
    hello_world()


#3
a = int(input("enter any num: "))

def even_or_odd():
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
even_or_odd()

#4
def print_pattern():
    for _ in range(3):
        print("******")   
print_pattern()

def a():
    for i in range(4):
        print(1 + i + 1)
#5
def print_diamond():
    for i in range(1, 5):  
        print(" " * (5 - i) + "*" * (2 * i - 1))
    for _ in range(2):  
        print(" " * 4 + "*")
print_diamond()





