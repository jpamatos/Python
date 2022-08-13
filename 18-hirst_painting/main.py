# import colorgram

# extraction = colorgram.extract("18-hirst_painting/images.jpg", 30)
# colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in extraction]
import turtle
import random

colors = [(58, 105, 148), (222, 234, 229), (225, 202, 110),
          (133, 85, 57), (220, 147, 74), (231, 224, 203), (143, 178, 201),
          (195, 145, 171), (235, 221, 231), (141, 78, 102), (212, 90, 65),
          (135, 181, 137), (64, 109, 91), (188, 82, 119), (151, 134, 66),
          (64, 157, 95), (43, 156, 190), (183, 191, 202), (216, 176, 191),
          (108, 121, 157), (7, 58, 104), (13, 68, 123), (156, 28, 38),
          (231, 174, 163), (173, 202, 183), (158, 203, 215), (174, 24, 17),
          (73, 57, 40), (78, 65, 46)]

turtle.colormode(255)
timmy = turtle.Turtle()  # Create timmy
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
# Moving timmy around
for i in range(12):  # Loop through lines
    timmy.setx(-320)
    timmy.sety(-270 + 50 * i)
    for _ in range(14):  # Loop through columns
        timmy.dot(20, random.choice(colors))
        timmy.setheading(0)
        timmy.forward(50)
# Create screen
screen = turtle.Screen()
screen.exitonclick()
