# My first attempt

# first_number = float(input("Enter the first number: "))
# second_number = float(input("Enter the second number: "))
# print(f"{first_number} * {second_number} = {first_number * second_number}")


# Book solution uses functions

def multiply(first, second):
    return first * second

def get_number(prompt):
    return float(input(prompt))

first_number = get_number("Enter the first number: ")
second_number = get_number("Enter the second number: ")
print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")