# EXERCISE 1
# Write Python code to print the seventh number of range(0, 25, 3).

given_range = range(0, 25, 3)

# Implementation 0: Easiest, Index
print(given_range[6])

# Implementation 1: Easy, List
# Remember the nth element is at index n - 1
print(list(given_range)[6])

# Implementation 2: Using lazy sequence attributes
print([number for i, number in enumerate(given_range) if i == 6][0])
