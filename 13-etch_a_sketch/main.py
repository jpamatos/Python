from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    """Move Timmy forward 10 steps"""
    timmy.forward(10)


def move_backward():
    """Move Timmy backward 10 steps"""
    timmy.backward(10)


def rotate_right():
    """Rotate Timmy right 10 degrees"""
    timmy.right(10)


def rotate_left():
    """Rotate Timmy left 10 degrees"""
    timmy.left(10)


screen.listen()  # listen to keyboard strokes

# Move turtle with W/S and A/D
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_right, "d")
screen.onkey(rotate_left, "a")

# Reset screen
screen.onkey(screen.reset, "c")
screen.exitonclick()
