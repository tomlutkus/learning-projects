'''
Chose your difficulty
Normal 😎: Use all Hints below to complete the project.
Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
Expert 🤯: Only use Hint 1 to complete the project.

Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
'''

# Prompt: Do you want to play a game of Blackjack? y/n
    # n: ends
    # y: starts

# Your cards: [0, 1, 2], current score: sum
# Computer's first card: 10

# Type 'y' to get another card, type 'n' to pass:
    # n: Computer's final hand: [0, 1], final score: sum
    # You win / You lose / Draw / Lose, opponent has blackjack

# loop back to "want to play"
from random import choice

all_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def ask_if_play():
    play_a_game = input("Do you want to play a game of Blackjack? (y/n)\n> ")
    if play_a_game == 'y':
        return True
    return False

def get_another_card():
    another_card = input("Type 'y' to get another card, type 'n' to pass.\n> ")
    if another_card == 'y':
        return draw_card(all_cards)
    else:
        



def draw_card(cards):
    return random.choice(cards)

keep_playing = ask_if_play()
while keep_playing:
    game_over = False

    while not game_over:
        player_cards = [draw_card(all_cards), draw_card(all_cards)]
        computer_cards = [draw_card(all_cards)]
        player_score = sum(player_cards)
        computer_score = sum(computer_score)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if player_score < 21:
            input



