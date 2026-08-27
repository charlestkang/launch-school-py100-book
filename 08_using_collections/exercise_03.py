# EXERCISE 3
# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse 
# order from the original. It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

given_tuple = (1, 2, 3, 4, 5)

# Method 1: Tuple Slicing
reversed_tuple_1 = given_tuple[-2: 0: -1]
print(reversed_tuple_1)

# Method 2: List Conversion
reversed_tuple_2 = list(reversed(given_tuple))
reversed_tuple_2.pop()
reversed_tuple_2.pop(0)
reversed_tuple_2 = tuple(reversed_tuple_2)
print(reversed_tuple_2)
