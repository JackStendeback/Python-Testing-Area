import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(238, 221, 62), (36, 99, 148), (241, 225, 229), (167, 61, 45), (182, 45, 62), (157, 167, 60),
              (114, 176, 147), (231, 238, 244), (63, 55, 48), (41, 119, 79), (206, 149, 90), (51, 58, 90),
              (199, 68, 95), (172, 127, 157), (205, 99, 64), (125, 103, 165), (46, 47, 61), (38, 163, 202),
              (91, 50, 65), (159, 35, 30), (36, 82, 66), (35, 71, 53), (121, 167, 192), (55, 48, 54),
              (91, 156, 105), (226, 172, 181), (233, 172, 162), (170, 205, 186)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
