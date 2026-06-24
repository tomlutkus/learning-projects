"""
higher_lower_game.py - Who has more followers?
Author: Thomas Lutkus
"""

from game_data import data
from art import logo, vs
from random import sample
from os import system

def fetch_a_b(data_list: list[dict]) -> tuple[dict, dict]:
    candidate_a, candidate_b = sample(data_list, 2)
    return candidate_a, candidate_b

def check_answer(a: dict, b: dict, user_input: str) -> bool:
    if a["follower_count"] > b["follower_count"]:
        winner = "a"
    else:
        winner = "b"
    if user_input == winner:
        return True
    return False

def user_choice() -> str:
    while True:
        user_input = input(
                "Who has more followers? Type 'A' or 'B':\n> "
            ).lower()
        if user_input in ("a", "b"):
            return user_input
        print("ERROR: Invalid input.")

def display(a: dict, b: dict):
    name_a = a["name"]
    desc_a = a["description"]
    country_a = a["country"]
    name_b = b["name"]
    desc_b = b["description"]
    country_b = b["country"]
    print(f"Compare A: {name_a}, {desc_a} from {country_a}.")
    print(vs)
    print(f"Against B: {name_b}, {desc_b} from {country_b}.")

def main():
    play = True
    score = 0
    while play:
        system('clear')
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        candidate_a, candidate_b = fetch_a_b(data)

        display(candidate_a, candidate_b)

        user_input = user_choice()
        user_right = check_answer(candidate_a, candidate_b, user_input)

        if user_right:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            try_again = input("Play again? Y/N\n> ").lower()
            score = 0
            if try_again == "n":
                play = False    

if __name__ == "__main__":
    main()