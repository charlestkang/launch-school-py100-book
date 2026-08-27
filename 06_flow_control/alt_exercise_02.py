# EXERCISE 2
# Write a function, even_or_odd, that determines whether its argument is an even or odd number.
# If it's even, the function should print 'even'; otherwise, it should print 'odd'. 
# Assume the argument is always an integer.

def even_or_odd(n):
    print("even" if n % 2 == 0 else "odd")

# Testing

even_or_odd(int(input("Pick a number to determine whether it is even or odd:\n")))
