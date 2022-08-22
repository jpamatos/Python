# A game of finding treasure in an island

# Start
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First Decision
decision = input('''You\'re at a cross road.
Where do you want to go? Type "left" or "right"\n''').lower()
if decision == "left":

    # Second Decision
    decision = input('''You\'ve come to a lake.
There is an island in the middle of the lake.
Type "wait" to wait for a boat Type "swin" to swin across.\n''').lower()
    if decision == "wait":

        # Final Decision
        decision = input('''You arrive at the island unharmed.
There is a house with 3 doors. One red, one yellow and one blue.
Which color do you choose?\n''').lower()
        if decision == "red":
            print("It's a room full of fire. Game Over")
        elif decision == "yellow":
            print("You found the treasure! You Win")
        elif decision == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exists. Game Over.")
    else:
        print("You got attacked by an angry torut. Game Over.")
else:
    print("You fell into a hole. Game Over.")
