from art import logo
import random
import os


def start():
    """Start a game of BlackJack"""
    is_game_over = False
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    is_game_over = compare(user_cards, computer_cards)

    while not is_game_over:
        decision = input("Do you want to draw a card?\n(y/n): ").lower()
        if decision == "y":
            user_cards.append(deal_card())
            is_game_over = compare(user_cards, computer_cards)
        elif decision == "n":
            while not is_game_over:
                computer_cards.append(deal_card())
                is_game_over = compare_dealer(user_cards, computer_cards)
            decision2 = input("Do you want to start another"
                              " game?\n(y/n): ").lower()
            if decision2 == "y":
                os.system("cls")
                start()
            elif decision2 == "n":
                return


def compare(user_cards, computer_cards):
    """Compare the score of player's and computer's hand"""
    print(f"Your cards: {user_cards}, sum: {calculate_score(user_cards)}"
          f"\nDealer cards: {computer_cards},"
          f"sum: {calculate_score(computer_cards)}")
    if ((calculate_score(user_cards) == 21) or
            (calculate_score(computer_cards) > 21)):
        print("You Win!")
        return True
    elif ((calculate_score(computer_cards) == 21) or
            (calculate_score(user_cards) > 21)):
        print("Dealer Wins!")
        return True
    else:
        return False


def compare_dealer(user_cards, computer_cards):
    """Check if dealer wins"""
    print(f"Your cards: {user_cards}, sum: {calculate_score(user_cards)}"
          f"\nDealer cards: {computer_cards}, "
          f"sum: {calculate_score(computer_cards)}")
    if (calculate_score(computer_cards) > 21):
        print("You Win!")
        return True
    elif ((calculate_score(computer_cards) == 21) or
            (calculate_score(user_cards) > 21)):
        print("Dealer Wins!")
        return True
    else:
        return False


def calculate_score(hand):
    """Calculate hand's score"""
    score = sum(hand)
    if score > 21:
        while 11 in hand:
            i = hand.index(11)
            hand[i] = 1
            score = sum(hand)
    return score


def deal_card():
    """Deal a card"""
    return random.choice(cards)


print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start()
