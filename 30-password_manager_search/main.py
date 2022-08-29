from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ----------------------- #
def generate_password():
    """Randomly generate a password"""
    # Letters, numbers and sylbols to generate a password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generating password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pass_list = password_letters + password_symbols + password_numbers
    shuffle(pass_list)
    password = "".join(pass_list)

    # Inster password on password entry
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy password to clipboard


# ---------------------------- SAVE PASSWORD ---------------------------- #
def save():
    """Save password information in a file called data.txt in append mode"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirmation = f"These are the details entered: \nEmail: {email}\n" + \
        f"Password: {password}\nIs it ok to save?"
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't left any "
                            "fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=confirmation)

        if is_ok:
            # Opening a file and saving the password there
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Focus cursos to star on webiste entry
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jean@gmail.com")  # Insert an email in email entry
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
