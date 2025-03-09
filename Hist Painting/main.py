import random

import colorgram
import turtle as turtle_module
import random


# rgb_colors = []
# colors = colorgram.extract("images.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [(140, 165, 192),
 (211, 155, 116), (23, 37, 56), (192, 142, 152),
 (60, 102, 134), (148, 69, 58), (231, 212, 107),
 (143, 177, 162), (141, 68, 77), (145, 28, 35), (46, 36, 32),
 (46, 32, 37), (66, 110, 96), (33, 51, 46), (135, 32, 27),
 (227, 168, 174), (234, 169, 161), (186, 98, 107),
 (194, 95, 82), (175, 188, 216), (18, 92, 69), (110, 124, 158), (33, 61, 105),
 (173, 203, 193), (21, 79, 98), (60, 149, 185)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 420

for dot_count in range(1,number_of_dots+1):
    tim.dot(10, random.choice(color_list))
    tim.forward(15)

    if dot_count % 30 == 0:
        tim.setheading(90)
        tim.forward(15)
        tim.setheading(180)
        tim.forward(450)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()