# import colorgram

# rgb_colors = []
# colors = colorgram.extract('proyectos\\18_hirst_painting\\image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
color_list = [(248, 248, 243), (207, 207, 108), (226, 226, 229), (243, 243, 232), (125, 125, 193), (33, 33, 151), (132, 132, 153), (142, 142, 57), (203, 203, 151), (229, 229, 117), (211, 211, 232), (156, 156, 78), (206, 206, 97), (43, 43, 88), (219, 219, 61), (174, 174, 59), (69, 69, 115), (235, 235, 174), (157, 157, 46), (165, 165, 186), (38, 38, 188), (233, 233, 161), (16, 16, 73), (18, 18, 64), (71, 71, 29), (140, 140, 29), (22, 22, 46), (71, 71, 47), (161, 161, 214), (10, 10, 106)]
tim.setheading(220)
tim.forward(340)
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