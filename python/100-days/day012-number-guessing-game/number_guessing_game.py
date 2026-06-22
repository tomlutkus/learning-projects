"""
number_guessing_game.py - Guess the number!
Author: Thomas Lutkus
"""

from art import logo
import sys
import os
import random

def think_a_number() -> int:
    return random.randint(1, 100)

def choose_difficulty() -> int:
    difficulty: str = input(
        "Choose a difficulty. Type 'easy' or 'hard':\n> "
    )
    if difficulty == "hard":
        return 5
    else:
        return 10

def guess_number() -> int:
    number_guess = input(
        "Make a guess:\n> "
    )
    try:
        number = int(number_guess)
    except ValueError:
        print("ERROR: the guess must be an integer between 1 and 100.")
        sys.exit(1)
    return number

def check_guess(attempts: int, number_to_guess: int) -> bool:
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = guess_number()
        if guess > number_to_guess:
            print("Too high.")
            attempts -= 1
        elif guess < number_to_guess:
            print("Too low.")
            attempts -= 1
        elif guess == number_to_guess:
            print(f"You got it! The answer is {number_to_guess}")
            return True
    print("You've run out of guesses.")
    return False

def main():
    score: int = 0
    games_played: int = 0
    while True:
        os.system('clear')
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        attempts = choose_difficulty()
        number_to_guess = think_a_number()
        guessed_it = check_guess(attempts, number_to_guess)
        if guessed_it:
            score += 1
        games_played += 1
        print(
            f"You played {games_played} games and won {score} so far."
        )
        new_game: str = input("New game? (y/n)\n> ")
        if new_game == "n":
            print("Thanks for playing! Good bye!")
            break
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Usage: python3 number_guessing_game.py")
        sys.exit(1)
    main()
