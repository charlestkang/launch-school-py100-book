# EXERCISE 11
# Challenging Problem: Don't feel bad if you struggle with this problem or can't solve it. The
# problem is not easy.
# It is designed to demonstrate why we prefer to use for loops when we can, and a big part of
# that problem is messy
# code that is difficult to write and understand. See how far you can get, but don't spend much
# time struggling.
# Print all of the even numbers in the following list of nested lists. This time, don't use any
# for loops.

# Copy Code
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
# Expected OutputCopy Code
# 6
# 4
# 2
# 4
# 16
# 0

outer_index = 0
inner_index = 0

while outer_index < len(my_list):
    while inner_index < len(my_list[outer_index]):
        n = my_list[outer_index][inner_index]
        if n % 2 == 0: print(n)
        inner_index += 1
    outer_index += 1
    inner_index = 0
