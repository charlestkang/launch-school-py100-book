# EXERCISE 7
# Without running the following code, identify the numbers that are included in each of the following 
# ranges:

# Copy Code
r1 = range(7)
r2 = range(1, 6)
r3 = range(3, 15, 4)
r4 = range(3, 8, -1)
r5 = range(8, 3, -1)

print('range(7) contains 0, 1, 2, 3, 4, 5, 6')
print('range(1, 6) contains 1, 2, 3, 4, 5')
print('range(3, 15, 4) contains 3, 7, 11')
print('range(3, 8, -1) is empty')
print('range(8, 3, -1) contains 8, 7, 6, 5, 4')

# Confirmation
print()
print('Confirmation')
ranges = [r1, r2, r3, r4, r5]
for item in ranges:
    print(list(item))
