from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    """Track a Scoreboard on screen"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        """Update scoreboard"""
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase(self):
        """Increase score by 1"""
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        """Write a game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
