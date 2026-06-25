"""
cofee_machine.py - Coffee is served!
Author: Thomas Lutkus
"""

from resources import MENU, resources
from os import system

def selection_menu() -> str:
    while True:
        selection_prompt = input(
            "What would you like? (espresso, latte, cappuccino)\n> "
        )
        if selection_prompt in (
            "off", "report", "espresso", "latte", "cappuccino"
            ):
            return selection_prompt

def issue_report(resources, money_stored):
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: ${money_stored}")

def check_resources(user_choice, menu, resources) -> tuple[bool, list[str]]:
    enough_resources = True
    insufficient_resources = []

    for ingredient, amount in menu[user_choice]["ingredients"].items():
        if amount > resources[ingredient]:
            enough_resources = False
            insufficient_resources.append(ingredient)            
    
    insufficient_string = ", ".join(insufficient_resources)
    return enough_resources, insufficient_string

def process_coins() -> float:
        inserted_coins = {
            "quarters": 0,
            "dimes": 0,
            "nickles": 0,
            "pennies": 0,
        }
        total = 0.00
        inserted_coins["quarters"] = int(input(
            "How many quarters?\n> "
        ))
        inserted_coins["dimes"] = int(input(
            "How many dimes?\n> "
        ))
        inserted_coins["nickles"] = int(input(
            "How many nickles?\n> "
        ))
        inserted_coins["pennies"] = int(input(
            "How many pennies?\n> "
        ))
        for coin, amount in inserted_coins.items():
            if coin == "quarters":
                total += amount * 0.25
            elif coin == "dimes":
                total += amount * 0.10
            elif coin == "nickles":
                total += amount * 0.05
            else:
                total += amount * 0.01
        return total


def process_transaction(money_provided, user_choice, menu) -> tuple[
    bool, float, float]:
        if money_provided < menu[user_choice]["cost"]:
            return False, None, None
        transaction_ok = True
        add_money = menu[user_choice]["cost"]
        refund = money_provided - menu[user_choice]["cost"]
        return True, add_money, refund


def make_coffee(user_choice):
    print(f"{user_choice} served.")

def main():
    powered_on = True
    money_stored = 0.00

    while powered_on:
        system('clear')
        # Prompt the user by asking "what would you like? (espresso, late, cappuccino)
        user_choice = selection_menu()

        if user_choice == "off":
            # Turn off the Coffee Machine by entering “off” to the prompt
            powered_on = False
            exit(0)
        elif user_choice == "report":
            # Print report of resources when user enters "report" to the prompt
            issue_report(resources, money_stored)
        elif user_choice in ("espresso", "latte", "cappuccino"):
            enough_resources, insufficient = check_resources(
                user_choice, MENU, resources
                )
            # Check resources sufficient
            if not enough_resources:
                print(f"Sorry, there is not enough {insufficient}")
                continue
            print("Please insert coins.")
            money_provided = process_coins()
            transaction_ok, add_money, refund = process_transaction(
                money_provided, user_choice, MENU
                )
            if transaction_ok:
                if refund == 0.00:
                    print("You paid the exact amount, no change.")
                else:
                    print(f"Here is ${refund:.2f} change.")
                make_coffee(user_choice)
            else:
                print("Sorry, that's not enough money. Money refunded.")
            input("Press any key to conclude order.")

        
if __name__ == "__main__":
    main()