from turtle import Turtle


class Scoreboard(Turtle):
    """Create a scoreboard to track the player's score"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updade score for both players"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score,
                   align="center",
                   font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score,
                   align="center",
                   font=("Courier", 80, "normal"))

    def l_point(self):
        """Add a point to left player"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Add a point to right player"""
        self.r_score += 1
        self.update_scoreboard()
