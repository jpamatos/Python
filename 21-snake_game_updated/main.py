from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

# Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create actors
snake = Snake()
food = Food()
score = Score()

# Wait for keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# The game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Detect collision with food
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    # Detect collision with food
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
            snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

# Close window
screen.exitonclick()
