import sys
from art import logo

def calculator(n1, n2, op):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2

def main():
    new_calculation = True
    result = None

    while True:
        if new_calculation:
            sys.stdout.write('\033[2J\033[H')
            sys.stdout.flush()
            print(logo)
            first_number = float(input("What's the first number? "))
        else:
            first_number = result
        operations = ["+", "-", "*", "/"]
        for operation in operations:
            print(f"{operation}")

        chosen_operation = input("Pick an operation: ")
        if chosen_operation not in operations:
            input("Invalid operation. Press <ENTER> to restart program.")
            new_calculation = True
            continue
        second_number = float(input("What's the second number? "))

        result = calculator(first_number, second_number, chosen_operation)
        print(f"{first_number} {operation} {second_number} = {result}")

        use_result = input(
            f"Type 'y' to continue calculating with {result}, "
            "or type 'n' to start a new calculation: "
        )
        if use_result == "y":
            new_calculation = False
        else:
            new_calculation = True


if __name__ == "__main__":
    main()
