# Draw a triangle, queare, pentagon, hexagon, heptagon, octagon, nonagon and decagon.

from turtle import Turtle, Screen
import random

tim = Turtle()

# def forms():
#     angle = 3
#     while angle < 11:
#         form = 360 / angle
#         for _ in range(angle):
#             tim.right(form)
#             tim.forward(90)
#         angle += 1

# forms()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeanGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
