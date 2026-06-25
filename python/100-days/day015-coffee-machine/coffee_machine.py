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
    
    return enough_resources, insufficient_resources

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

def process_transaction(money_provided, user_choice, menu):
        if money_provided < menu[user_choice]["cost"]:
            return False, None, None
        add_money = menu[user_choice]["cost"]
        refund = money_provided - menu[user_choice]["cost"]
        return True, add_money, refund

def make_coffee(user_choice, menu, resources):
    ingredients = menu[user_choice]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    print(f"Here is your {user_choice}. Enjoy!")

def handle_order(user_choice, menu, resources):
    enough_resources, insufficient_resources = check_resources(
                user_choice, menu, resources
                )
    if not enough_resources:
        print("Sorry, there is not enough:")
        for resource in insufficient_resources:
            print(f"- {resource}")
        print("Please, choose another product.\n")
        input("Press ENTER to continue.")
        return 0
    cost = menu[user_choice]["cost"]
    print(f"{user_choice} costs ${cost}.")
    print("Please insert coins.")
    money_provided = process_coins()
    transaction_ok, add_money, refund = process_transaction(
        money_provided, user_choice, menu
        )
    if transaction_ok:
        if refund == 0.00:
            print("You paid the exact amount, no change.\n")
        else:
            print(f"Here is ${refund:.2f} change.\n")
        make_coffee(user_choice, menu, resources)
        input("Press ENTER to conclude order.")
        return add_money
    else:
        print("Sorry, that's not enough money. Money refunded.\n")
        input("Press ENTER to try ordering again.")
        return 0

def main():
    money_stored = 0.00
    powered_on = True
    while powered_on:
        system('clear')
        user_choice = selection_menu()
        if user_choice == "off":
            print("Administrator: power off requested, powering off...\n")
            exit(0)
        elif user_choice == "report":
            print("Administrator: report requested, issuing report...\n")
            issue_report(resources, money_stored)
            input("Press ENTER to continue.")
        elif user_choice in ("espresso", "latte", "cappuccino"):
            add_money = handle_order(user_choice, MENU, resources)
            money_stored += add_money

        
if __name__ == "__main__":
    main()