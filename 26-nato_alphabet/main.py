import pandas as pd

# Read data with the nato alphabet
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Dictionary comprehension to create a nato alphabet from file
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    """Get a word from user"""
    word = input("Enter a word: ").upper()

    # List comprehension to spell user's word in phonetic alphabet
    try:
        nato = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato)


generate_phonetic()
