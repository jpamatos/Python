# Import art for logo
from art import logo

def cipher():
    """Start the Caesar Cipher"""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(text, shift, direction)
    question = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if question == "yes":
        cipher()
    elif question == "no":
        print("Program ended.")

def ceasar(text, shift, direction):
    """Enconde or decode the text in the cipher"""
    if direction == "decode":
            shift *= -1
    for i in range(len(text)):
        if text[i] in alphabet:
            index = alphabet.index(text[i])
            index += shift
            text = text[:i] + alphabet[index] + text[i + 1:]
    print(f"The {direction}d text is: {text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
cipher()


