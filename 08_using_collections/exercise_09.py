# EXERCISE 9
# Write some code to replace the value 6 in the following nested list with 606:

# Copy Code
# stuff = [
#     ['hello', 'world'],
#     ['example', 'mem', None, 6, 88],
#     [4, 8, 12],
# ]
# You don't have to search the list. Just write an assignment that replaces the 6.

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
new_stuff = list(stuff)

stuff[1][3] = 606

print(stuff)


# Just for fun!
stuff = new_stuff
for item in stuff:
    for thing in item:
        thing = 606 if thing == 6 else thing
print(stuff)
