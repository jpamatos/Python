from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/deutsch.csv")

data = df.to_dict(orient="records")
current_card = {}


def next_card():
    """Pick a random card from dataframe of words"""
    global current_card, timer
    window.after_cancel(timer)  # Clear timer

    # Get a random card
    current_card = random.choice(data)
    canvas.itemconfig(title, text="German", fill="black")
    canvas.itemconfig(word, text=current_card["German"], fill="black")
    canvas.itemconfig(card, image=card_front)

    # Start a 3 second timer after getting a new card
    timer = window.after(3000, func=flip_card)


def flip_card():
    """Flip the card to show english translation side"""
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=card_back)


def is_known():
    """Remove a known word from the list of words to learn
    and save them in a csv"""
    data.remove(current_card)
    new_csv = pd.DataFrame(data)
    new_csv.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Create Window
window = Tk()
window.title("FlashApp")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create flipped side
timer = window.after(3000, func=flip_card)

# Create canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150,
                           text="Title",
                           font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263,
                          text="word",
                          font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create unknow button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,
                        highlightthickness=0,
                        command=next_card)
unknown_button.grid(row=1, column=0)

# Create know button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,
                      highlightthickness=0,
                      command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
