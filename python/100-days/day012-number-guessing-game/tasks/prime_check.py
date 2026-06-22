import sys

def check_if_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True

    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    
    return True

def main(number_input):
    try:
        number = int(number_input)
    except ValueError:
        raise ValueError("ERROR: Your input must be a positive integer.")
    is_prime = check_if_prime(number)
    if is_prime:
        print(f"The number {number} is a prime number.")
    else:
        print(f"The number {number} is not a prime number.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        number = input("Write an integer to test if prime:\n> ")
    elif len(sys.argv) == 2:
        number = sys.argv[1]
    else:
        print("Usage: python3 prime_check.py [NUMBER]")
        sys.exit(1)
    main(number)