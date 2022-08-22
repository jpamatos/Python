from art import logo
import os


def auction():
    """Start Auction"""
    print("Welcome to the secret auction program.")
    make_bid()


def make_bid():
    """A person makes a bid"""
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    decision = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if decision == "yes":
        os.system("cls")
        make_bid()
    elif decision == "no":
        result()


def result():
    """Result of Auction"""
    max_bid = 0
    max_bidder = ""
    for bidder, bid in bids.items():
        if bid > max_bid:
            max_bid = bid
            max_bidder = bidder
    print(f"The winner is {max_bidder} with a bid of ${max_bid}!")


print(logo)
bids = {}
auction()
