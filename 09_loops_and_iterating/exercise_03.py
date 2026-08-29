# EXERCISE 3
# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for 
# loop.

# Copy Code
my_list = [6, 3, 0, 11, 20, 4, 17]
# Expected Output
# Copy Code
# 6
# 3
# 0
# 11
 #20
# 4
# 17

print("while loop:")

idx = 0
while idx < len(my_list):
    print(my_list[idx])
    idx += 1

print("for loop:")

for n in my_list:
    print(n)
