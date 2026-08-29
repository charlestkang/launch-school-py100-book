# EXERCISE 6
# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. In this problem, you should write
# code that creates a new list with one element for each number in my_list. If the original number
# is an even, then the corresponding element in the new list should contain the string 'even';
# otherwise, the element should contain 'odd'.

# Copy Code
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
# Expected Output
# Copy Code
# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]

# Variation 1: Using for loop:
new_list_1 = []
for item in my_list:
    if item % 2 == 0:
        new_list_1.append('even')
    else: new_list_1.append('odd')

# Variation 2: Using list comprehension
new_list_2 = ['even' if n % 2 == 0 else 'odd' for n in my_list]

# Checking
print(new_list_1, new_list_2)
