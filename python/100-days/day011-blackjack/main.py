from random import choice
from os import system
from art import logo

all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(cards_list):
    return cards_list.append(choice(all_cards))

def score(cards_list):
    total = sum(cards_list)
    aces = cards_list.count(11)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def computer_play(computer_score, computer_cards):
    
    while computer_score < 17:
        draw_card(computer_cards)
        computer_score = score(computer_cards)
    return computer_score, computer_cards

def player_play(player_score, player_cards):
    player_round = True

    while player_round:
        ask_another_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
        if ask_another_card == 'y':
            draw_card(player_cards)
            player_score = score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            if player_score > 21:
                break
        else:
            player_round = False
    return player_score, player_cards

def deal():
    player_cards = []
    computer_cards = []
    for _ in range(2):
        draw_card(player_cards)
        draw_card(computer_cards)
    return player_cards, computer_cards

def final_hand(player_cards, computer_cards):
    player_score = score(player_cards)
    computer_score = score(computer_cards)
    player_hand = f"Your final hand: {player_cards}, final score: {player_score}"
    computer_hand = f"Computer's final hand: {computer_cards}, final score: {computer_score}"
    return player_hand, computer_hand

def determine_victor():
    player_cards, computer_cards = deal()
    player_score = score(player_cards)
    computer_score = score(computer_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    player_score, player_cards = player_play(player_score, player_cards)
    if player_score > 21:
        message = "You went over, you lose!"
    else:
        computer_score, computer_cards = computer_play(computer_score, computer_cards)
        if computer_score > 21:
            message = f"The computer went over, you win!"
        elif player_score > computer_score:
            message =  "Your score beats the computer's, you win!"
        elif player_score == computer_score:
            player_blackjack = len(player_cards) == 2 and player_score == 21
            computer_blackjack = len(computer_cards) == 2 and computer_score == 21
            if player_blackjack and not computer_blackjack:
                message = "Blackjack! You win!"
            elif computer_blackjack and not player_blackjack:
                message = "Computer has blackjack, you lose!"
            else:
                message = "It's a draw!"
        else:
            message = "The computer's score beats yours, you lose!"
    return message, player_cards, computer_cards

def main():
    play_game = True
    while play_game:
        ask_new_game = input("Do you want to play a game of blackjack? (y/n): ")
        if ask_new_game != "y":
            play_game = False
            break
        system("clear")
        print(logo)
        message, player_cards, computer_cards = determine_victor()
        player_hand, computer_hand = final_hand(player_cards, computer_cards)
        print(player_hand)
        print(computer_hand)
        print(message)

main()
