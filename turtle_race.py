import random
from turtle import Turtle, Screen

screen = Screen()
screen_width = 500
screen_height = 400
screen.setup(width=screen_width, height=screen_height)

colors = ["red","orange","yellow","green","blue","purple"]
no_of_turtle = 6
spacing_between_turtles = 30


def create_turtle(color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    return new_turtle


def go_to_start_line(turt_list):
    x = 20 - screen_width/2
    y = int((-no_of_turtle * spacing_between_turtles) / 2)
    for turt in turt_list:
        y = y +  spacing_between_turtles
        turt.goto(x=x, y=y)

    #turt.goto(x=pos_x_y[0], y= pos_x_y[1])



turtles = []
for color in colors:
    turtles.append(create_turtle(color))

go_to_start_line(turtles)


is_race_on = True

while is_race_on:
    for turt in turtles:
        random_distance = random.randint(0,10)
        turt.forward(random_distance)
        turt_x_posittion = turt.xcor()
        if turt_x_posittion >= int(screen_width/2) - 20:
            is_race_on = False
            print(f"Winner is : {turt.pencolor()} turtle")


screen.exitonclick()
