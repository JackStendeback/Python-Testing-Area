import turtle as t
import random

tim = t.Turtle()

colors = ["aquamarine", "deep sky blue", "sandy brown", "salmon", "medium slate blue", "light coral", "wheat",
          "SeaGreen", "IndianRed", "CornflowerBlue"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_size_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_size_n)
