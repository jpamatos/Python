from turtle import Turtle, Screen
import random

# Create game screen
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win "
                       "the race? Enter a color:")

# Create 7 turtles with different colors
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "teal", "purple"]
for i in range(7):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230, y=-90 + 30 * i)

# Game start
race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if bet == winner:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()  # Click to close game
