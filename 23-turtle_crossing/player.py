from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Create the player character"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)

    def go_up(self):
        """Move the turtle up"""
        self.forward(MOVE_DISTANCE)

    def crossed(self):
        """Detect if timmy crossed safely"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start(self):
        self.goto(STARTING_POSITION)
