from art import *
from game_data import data
import random
import os

def start():
    """Start the game of Higher Lower"""
    print(logo)
    score = 0
    end_game = False
    a = random_account()
    b = random_account()
    
    # game loop
    while not end_game:
        a = b
        b = random_account()

        # choose a different b if it is equals to a
        while a == b:
            b = random_account()
        
        # print A and B for player to choose
        print(f"Compare A: {formatted_print(a)}.")
        print(vs)
        print(f"Compare B: {formatted_print(b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_count = a["follower_count"]
        b_count = b["follower_count"]

        correct = check(guess, a_count, b_count)

        # clear terminal
        os.system("cls")
        print(logo)

        # Verify answer
        if correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            end_game = True
            print(f"Sorry, that's wrong. Final score: {score}")




def random_account():
    """Get a random account from data"""
    return random.choice(data)

def formatted_print(account):
    """Format a printable account datails"""
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

def check(guess, a, b):
    """Check user's guess againts follower number
    if True, they are right, if False, they got it
    wrong."""
    if a > b:
        return guess == "a"
    else:
        return guess == "b"


start()