from turtle import Turtle


class Ball(Turtle):
    """Create a ball to play the game with"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball"""
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        """Detect a collision and bounce back in the y axis"""
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        """Detect a collision and bounce back in the x axis"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset ball's bosition"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
