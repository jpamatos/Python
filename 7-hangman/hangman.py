import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

# Pick a random word from a list of words
word = random.choice(word_list)
display = ["_"] * len(word)
lives = 6
print(f"{' '.join(display)}")
print(stages[lives])


# Game loop
while True:
    # User make a guess
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    not_in_word = True

    for i in range(len(word)):
        if display[i] == guess:
            print("Letter already guessed.")
            break

    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            not_in_word = False
    
    # Word not found
    if not_in_word:
            lives -= 1
    
    print(f"{' '.join(display)}")
    print(stages[lives])

    # Win condition
    if "_" not in display:
        print("You win!")
        break
    
    # Defeat condition
    if lives == 0:
        print(f"You lose! Word was {word}")
        break
    



