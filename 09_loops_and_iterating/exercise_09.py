# EXERCISE 9
# Don't let the math scare you. This is a logic and syntax problem, not a math problem.
# Write a function that computes and returns the factorial of a number by using a for or while
# loop. The factorial of a positive integer n, signified by n!, is defined as the product of all
# integers between 1 and n, inclusive:

# n!	Expansion	Result
# 1!	1	1
# 2!	1 * 2	2
# 3!	1 * 2 * 3	6
# 4!	1 * 2 * 3 * 4	24
# 5!	1 * 2 * 3 * 4 * 5	120
# You may assume that the argument is always a positive integer.

print("Method 1: While loop")

def factorial(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

# Copy Code
print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

print("Method 2: For loop")

def factorial(n):
    r = 1
    for i in range(n, 0, -1):
        r *= i  
    return r

# Copy Code
print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

print("Method 3: Recursion")

def factorial(n):
    f = n
    if f == 1: return 1
    f = f * factorial(f - 1)
    return f

# Copy Code
print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000
