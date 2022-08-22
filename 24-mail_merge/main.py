PLACEHOLDER = "[name]"  # Placeholder to replace the names

# Get a list of names from a file
with open("Names/invited_names.txt") as file:
    names = file.readlines()

# Open the model invitation
with open("Letters/starting_letter.txt") as file:
    letter_model = file.read()

    # Create every letter using a name
    for name in names:
        letter = letter_model.replace(PLACEHOLDER, name.strip())
        with open(f"ReadyToSend/letter_for_{name.strip()}.txt", "w") \
                as final_letter:
            final_letter.write(letter)
