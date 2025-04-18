"""
Draeing app with below controls
W = Forward
S = Backward
A = Counter Clockwise
D = Clockwise
"""

from turtle import Turtle, Screen



tim = Turtle()

def forward():
    tim.forward(2)

def back_wards():
    tim.back(2)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()

screen.onkeypress(forward, key="W")
screen.onkeypress(back_wards, key="S")
screen.onkeypress(counter_clockwise, key="A")
screen.onkeypress(clockwise, key="D")
screen.onkeypress(clear, key="C")







screen.exitonclick()
