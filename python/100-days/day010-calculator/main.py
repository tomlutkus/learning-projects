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

new_calculation = True
result = None

while True:
    if new_calculation:
        sys.write('\033[2J\033[H')
        sys.flush()
        print(logo)
        first_number = float(input("What's the first number? "))
    else:
        first_number = result
    
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the second number? "))

    result = calculator(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {result}")

    use_result = input(
        f"Type 'y' to continue calculating with {result}, "
        "or type 'n' to start a new calculation: "
    )
    if use_result == "y":
        new_calculation = False
    else:
        new_calculation = True
