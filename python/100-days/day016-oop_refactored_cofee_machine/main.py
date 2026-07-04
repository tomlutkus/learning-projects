from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
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


def main():
    powered_on = True

    while powered_on:
        # The prompt should show again to serve the next customer.
        system('clear')
        system_menu = Menu()
        coffee_maker = CoffeeMaker()
        money_machine = MoneyMachine()

        # Prompt user by asking “What would you like? (espresso/latte/cappuccino/)
        user_choice = selection_menu()
        # Turn off the Coffee Machine by entering “off” to the prompt.
        if user_choice == "off":
            print("Powering off...")
            exit(0)

        # Print report
        elif user_choice == "report":
            print("Issuing report...")
            coffee_maker.report()
            money_machine.report()
            input("Press ENTER to continue")
        # Check resources sufficient?
        else:
            # coffee_maker.is_resource_suf
            print(f"{user_choice}")
            input("Press ENTER to continue")
        # Process coins.


        # Check transaction successful?


        # Make Coffee.

if __name__ == "__main__":
    main()
