from turtle import Turtle, Screen
import random


def random_direction():
    directions = ["north", "south", "east", "west"]
    direction = random.choice(directions)
    return direction


def random_color():
    color_list = []
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_list = [r, g, b]
    return color_list


screen = Screen()
screen.colormode(255)
jim = Turtle()
jim.pensize(10)
jim.speed(10)

random_walk_num = 100
for _ in range(random_walk_num):
    color = random_color()
    jim.pencolor(color[0], color[1], color[2])
    turtle_direction = random_direction()
    if turtle_direction == "north":
        jim.left(90)
        jim.forward(20)
    elif turtle_direction == "south":
        jim.right(90)
        jim.forward(20)
    elif turtle_direction == "east":
        jim.forward(20)
    else:
        jim.right(180)
        jim.forward(20)

screen.exitonclick()
