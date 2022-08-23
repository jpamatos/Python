import turtle
import pandas as pd

IMAGE = "blank_states_img.gif"  # Image path

# Set up Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Read data from file
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed = []

# Game loop break when the player guessed all states
while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)}/50 States Correct",
                              prompt="What's another state's name?").title()

    # If user wants to exit early, create a list of missing states
    if answer == "Exit":
        missing = [state for state in states if state not in guessed]
        data_frame = pd.DataFrame(missing)
        data_frame.to_csv("States_to_learn.csv")
        break

    # Check if the answer is correct and not already exists
    if answer in states and answer not in guessed:
        guessed.append(answer)

        # Setup written name
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Get coordinates from state and write on map
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
