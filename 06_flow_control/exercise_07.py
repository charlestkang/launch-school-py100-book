# EXERCISE 7
# Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0
# Copy Code
# number_range(0)     # 0 is between 0 and 50
# number_range(25)    # 25 is between 0 and 50
# number_range(50)    # 50 is between 0 and 50
# number_range(75)    # 75 is between 51 and 100
# number_range(100)   # 100 is between 51 and 100
# number_range(101)   # 101 is greater than 100
# number_range(-1)    # -1 is less than 0

def number_range(n):
    if 0 <= n <= 50:
        print(f"{n} is between 0 and 50")
    if 51 <= n <= 100:
        print(f"{n} is between 51 and 100")
    if n > 100:
        print(f"{n} is greater than 100")
    if n < 0:
        print(f"{n} is less than 0")

# Testing
number_range(int(input("Pick a number: ")))

# Smarter solution from the book:
def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')