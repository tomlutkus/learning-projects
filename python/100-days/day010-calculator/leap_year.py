'''
Leap year rules with examples

1. Add an extra day every 4 years
   `2000 / 4 = 500` → leap
   `2100 / 4 = 525` → leap

2. Skip it if it’s a new century
   `2000 / 100 = 20` → not leap
   `2100 / 100 = 21` → not leap

3. Unless the century is divisible by 400
   `2000 / 400 = 5` → leap
   `2100 / 400 = 5.25` → not leap
'''

def check_if_leap_year(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

    return False

while True:

    year = int(input("Enter the year to check if leap: "))
    is_leap = check_if_leap_year(year)

    if is_leap:
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")
    
    try_again = (input("Do you want to check another year? (y/n)\n> "))

    if try_again == "n":
        break
    
