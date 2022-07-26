from art import logo
import random, os



def start():
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    compare(user_cards, computer_cards)


    while True:
        if is_game_over:
                break
        decision = input("Do you want to draw a card?\n(y/n): ").lower()
        if decision == "y":
            user_cards.append(deal_card())
            compare(user_cards, computer_cards)
        elif decision == "n":
            decision2 = input("Do you want to start another game?\n(y/n): ").lower()
            if decision2 == "y":
                os.system("cls")
                start()
            elif decision2 == "n":
                return
    
def compare(user_cards, computer_cards):
    if calculate_score(user_cards) == 21 or calculate_score(computer_cards) > 21:
        print("You Win!")
        is_game_over = True
        print(is_game_over)
    elif calculate_score(computer_cards) == 21 or calculate_score(user_cards) > 21 :
        print("Dealer Wins!")
        is_game_over = True
        print(is_game_over)

    
    print(f"Your cards: {user_cards}, sum: {calculate_score(user_cards)}\nDealer cards: {computer_cards}, sum: {calculate_score(computer_cards)}")

def calculate_score(hand):
    score = sum(hand)
    if score > 21:
        while 11 in hand:
            i = hand.index(11)
            hand[i] = 1
            score = sum(hand)
    return score
    

def deal_card():
    return random.choice(cards)

is_game_over = False
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start()