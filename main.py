
# import colorgram
# colors = colorgram.extract("image.jpg", 10)
# color_list=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#
#     color_list.append(new_color)
#
#
# print(color_list)


import turtle
from turtle import Turtle
import random

tim=Turtle()
turtle.colormode(255)

color_list=[(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]

tim.speed("slowest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)

number_of_dots=100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






