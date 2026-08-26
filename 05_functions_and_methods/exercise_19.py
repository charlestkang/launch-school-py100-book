# EXERCISE 19
# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

# Copy Code
def remainders_5(numbers):
    return [number % 5 for number in numbers]
# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

# Copy Code
numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

arr_numbers = [numbers_1, numbers_2, numbers_3, numbers_4]

print("Given the following lists of numbers:")

for i, numbers in enumerate(arr_numbers, start=1):
    print(f"Array {i}: {numbers}")

print()
print("We evaluate whether the list does not contain any numbers that are divisible by 5:")

for numbers in arr_numbers:
    print(all(remainders_5(numbers)))

print()
print("We provide also a solution not using for loops or enumeration:")
print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
