from turtle import Turtle, Screen

# Had to install this via 'pip install heroes' from pypi.org
# Installing that way can be misleading as you may install to the wrong area.
# TODO: BEST PRACTICE: Find what you want on pypi, type import 'name' and let pycharm do the work(click red lightbulb)
import heroes
import villains

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


def turtle_square():
    for number in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


turtle_square()

screen = Screen()
screen.exitonclick()

print(heroes.gen())
print(villains.gen())
