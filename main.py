from turtle import Turtle,Screen

tim = Turtle()
tim.color("blue")
tim.forward(10)
def move():
    tim.forward(10)


screen = Screen()
screen.listen()
screen.onkeypress(move, key="space")
screen.exitonclick()