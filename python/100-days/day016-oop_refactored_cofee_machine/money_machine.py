class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self) -> None:
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def process_coins(self, cost) -> float:
        """Returns the total calculated from coins inserted."""
        print(f"Please insert coins. Your order costs {cost}")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}? ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost: float) -> bool:
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins(cost)
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            input("Press ENTER to continue")
            return True
        else:
            print("Sorry, that's not enough money. Refund issued.")
            self.money_received = 0
            input("Press ENTER to continue")
            return False