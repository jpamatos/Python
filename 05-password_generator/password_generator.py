# Import random package
import random

# Letters, numbers and sylbols to generate a password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")

# Select password specifics
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

# Generating password
pass_list = []
for _ in range(0, n_letters):
    pass_list.append(random.choice(letters))
for _ in range(0, n_symbols):
    pass_list.append(random.choice(symbols))
for _ in range(0, n_numbers):
    pass_list.append(random.choice(numbers))
random.shuffle(pass_list)
password = ""
for t in pass_list:
    password += t

# Print password
print("Here is your password: ", password)
