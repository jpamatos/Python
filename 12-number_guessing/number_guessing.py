import random
from art import logo

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def game():
    """Start GuessTheNumber game"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    n_guess = difficulty()

    # A number to guess is chosen randomly
    goal = random.randint(1, 100)

    # User makes a guess
    guess = 0

    while goal != guess:
        guess = int(input(f"You have {n_guess} attempts remaining to guess the number.\nMake a guess: "))

        n_guess = check(guess, goal, n_guess)

        if n_guess == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != goal:
            print("Guess again.")
        
    
def difficulty():
    """Set the difficulty of GuessTheNumber"""
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == "easy":
        return EASY_DIFFICULTY
    elif diff == "hard":
        return HARD_DIFFICULTY

def check(guess, goal, n_guess):
    """Check if user won or is close"""
    if guess == goal:
        print(f"You win! The number was {goal}")
    elif guess > goal:
        print("Too high")
        return n_guess - 1
    else:
        print("too low")
        return n_guess - 1

game()