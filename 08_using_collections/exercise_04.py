# EXERCISE 4
# This is a 3-part question. Consider the following dictionary:

# Copy Code
# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }
# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
# Part 2: Write some code to print None when you try to print the value associated with the 
# non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you try to print the value associated with the 
# non-existent key, Lizard.


pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}
print(f"Given dict: {pets}")
print()

# Part 1: 
print("Part 1: Print Bark by accessing element associated with key Dog")
print(pets['Dog'])
print()

# Part 2:
# Implementation 1: 
print("Part 2: Print None when try to print value associated with nonexistent key 'Lizard'")
print(pets['Lizard']) if 'Lizard' in pets.keys() else print(None)
print()

# Implementation 2:
print("Part 2: Print None when try to print value associated with nonexistent key 'Lizard'")
try:
    print(pets['Lizard'])
except KeyError:
    print(None)
print()

# Implementation 3 (book):
print("Part 2: Print None when try to print value associated with nonexistent key 'Lizard'")
print(pets.get('Lizard'))
print()

# Part 3:
# Implementation 1:
print("Part 3: Print <silence> when try to print value associated with nonexistent key 'Lizard'")
print(pets['Lizard']) if 'Lizard' in pets.keys() else print("<silence>")
print()

# Implementation 2 (book):
print("Part 3: Print <silence> when try to print value associated with nonexistent key 'Lizard'")
print(pets.get('Lizard', '<silence>'))
