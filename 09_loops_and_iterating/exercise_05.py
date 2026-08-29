# EXERCISE 5
# Print all of the even numbers in the following list of nested lists. Don't use any while loops.

# Copy Code
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
# Expected Output
# Copy Code
# 6
# 4
# 2
# 4
# 16
# 0

for list in my_list:
    for item in list:
        if item % 2 == 0: 
            print(item)
