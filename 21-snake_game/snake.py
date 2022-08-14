from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """Create a Snake to play the game, the initial snake has 3 segments"""

    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

    def create_segments(self):
        """Create a segments with 3 segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a segment to snake"""
        body = Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.segments.append(body)

    def extend(self):
        """Extend the snake by 1 segment"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the segments using the last segment position"""
        for segment in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment - 1].xcor()
            y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Make the snake move north"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Make the snake move south"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Make the snake move west"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Make the snake move east"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
