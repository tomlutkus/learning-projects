"""
OOP Coffee Machine - Coffee is served!
Author: Thomas Lutkus
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

def main() -> None:
    powered_on = True
    while powered_on:
        # Start fresh on a new order
        system('clear')
        system_menu = Menu()
        # Prompt user with the available menu choices
        menu_options = system_menu.get_items()
        selection: str = input(
                f"What would you like? ({menu_options})\n> "
            )
        # Turn off the Coffee Machine by entering “off” to the prompt
        if selection == "off":
            print("Powering off...")
            exit(0)
        # Print a report by entering "report" to the prompt
        elif selection == "report":
            print("Issuing report...")
            coffee_maker.report()
            money_machine.report()
            input("Press ENTER to continue")
            continue
        # Check if the entered selection is available
        else:
            item = system_menu.find_drink(selection)
        if not item:
            print(f"Sorry, that item is not available.")
            input("Press ENTER to continue")
            continue
        # Check resources sufficient?
        payment_received = False
        if coffee_maker.is_resource_sufficient(item):
            # Process coins.
            payment_received = money_machine.make_payment(item.cost)
        # Check transaction successful?
        if payment_received:
            # Make Coffee.
            coffee_maker.make_coffee(item)


if __name__ == "__main__":
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    main()
