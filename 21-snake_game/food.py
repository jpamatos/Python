from turtle import Turtle
import random


class Food(Turtle):
    """Create a food object that will be eaten by the snake"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Randomly refreshes food's position"""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
