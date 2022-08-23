import pandas as pd

# Read data with the nato alphabet
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Dictionary comprehension to create a nato alphabet from file
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# Get user name
name = input("Enter a word: ").upper()

# List comprehension to spell user's name in phonetic alphabet
nato = [alphabet[letter] for letter in name]
print(nato)
