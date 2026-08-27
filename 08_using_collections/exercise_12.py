# EXERCISE 12
# Write some code that determines and prints whether the number 3 appears inside each of these lists:

# Copy Code
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']
# You should print True or False depending on each result.
num_array = [numbers1, numbers2, numbers3, numbers4, numbers5]
for num in num_array:
    print(3 in num)
