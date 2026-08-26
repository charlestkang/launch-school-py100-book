# EXERCISE 18
# The following function returns a list of the remainders of dividing the numbers in numbers by 3:

# Copy Code
def remainders_3(numbers):
    return [number % 3 for number in numbers]
# Use this function to determine which of the following lists contains at least one number that is NOT evenly divisible by 3 (that is, the remainder is not 0):

# Copy Code
numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []
# Note: when working with integers, a value of 0 is "falsy"; all other integers are "truthy".


# ANSWER:
num_arrays = [numbers_1, numbers_2, numbers_3, numbers_4]
for arr in num_arrays:
    if any(remainders_3(arr)):
        print(f"{arr} contains at least one number not evenly divisible by 3.")
    else:
        print(f"{arr} contains only numbers that are evenly divisible by 3.")

print()
print("Solution without for loop:")
# Solution without for loop:
print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))

print()
print("Solution with a comprehension:")
# Solution with a comprehension
print([any(remainders_3(arr)) for arr in num_arrays])