############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear

def deal_card():
    '''Returns a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user, computer):
    if user == computer:
        return("Its a draw 😒")
    elif computer == 0:
        return("You Lose 😢")
    elif user == 0:
        return("BlackJack you win!😁")
    elif user > 21:
        return("You went over you lose 😢")
    elif computer > 21:
        return("Dealer busted you win! 😁")
    elif computer > user:
        return("Computer scored higher you lose 😢")
    else:
        return("You scored higher you win! 😁")

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    print(logo)

    while not is_game_over:
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
        
        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score > 21 or user_score == 0 or computer_score == 0:
                is_game_over = True
            else:
                proceed = input("Do you want another card?\nType 'y' for yes and 'n' for no: ")
                if proceed == 'y':
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)


        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))


while input("\nDo you want to play a game of blackjack?\nType 'y' for yes and 'n' for no:  ") == 'y':
    clear()
    play_game()