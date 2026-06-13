from art import logo
import sys # To clear the scren

print(logo)

def collect_bids() -> dict[str, int]:
    collected_bids: dict[str, int] = {}
    more_bidders: bool = True

    while more_bidders:

        user_name: str = input("What is your name?\n> ")
        user_bid: int = int(input("What is your bid\n$"))
        collected_bids[user_name] = user_bid

        ask_if_more: str = input(
            "Are there any other bidders? yes/no\n> "
            ).lower()

        # Clears the screen
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()

        # Ends the loop if no was chosen
        if ask_if_more == "no":
            more_bidders = False

    return collected_bids


def compare_bids(bids_dictionary: dict[str, int]) -> tuple[str | None, int | float]:
    highest_bid: tuple[str | None, int | float] = (None, float("-inf"))

    for name in bids_dictionary:

        # Tie-breaker: first to submit takes it
        if bids_dictionary[name] > highest_bid[1]:
            highest_bid = (name, bids_dictionary[name])

    return highest_bid

bids = collect_bids()
winner, amount = compare_bids(bids)

print(f"The winner is {winner} with a bid of ${amount}!")