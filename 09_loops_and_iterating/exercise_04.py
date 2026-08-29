# EXERCISE 4
# Use a while loop to print all numbers in my_list with even values, one number per line. Then,
# print the odd numbers using a ' for' loop.

# Copy Code
my_list = [6, 3, 0, 11, 20, 4, 17]
# Expected Even Values
# Copy Code
# 6
# 0
# 20
# 4
# Expected Odd Values
# Copy Code
# 3
# 11
# 17

print("All even values in my_list with while loop:")

idx = 0
while idx < len(my_list):
    if my_list[idx] % 2 == 0:
        print(my_list[idx])
    idx += 1

print("All odd values in my_list with for loop:")

for n in my_list:
    if n % 2 != 0: print(n)
