# Import random package
import random

# rock move
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# paper move
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# scissors move
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Player choose a move
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for "
                   "Scissors.\n"))
print("You chose: ")
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)

# Computer chose a move randomly
computer = random.randint(0, 2)
print("Computer chose: ")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

# Game result
if player == computer:
    print("It's a draw!")
else:
    if (player == computer + 1) or (player == 0 and computer == 2):
        print("You win!")
    else:
        print("You lose!")
