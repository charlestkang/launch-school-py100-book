# EXERCISE 2

# This question may be a little challenging if your math skills are rusty. 
# Don't be afraid to take advantage of the hints. 
# Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
# Each digit may require multiple Python statements.

x = 4936
ones = x % 10
x = x // 10
tens = x % 10
x = x // 10
hundreds = x % 10
x = x // 10
thousands = x % 10

print(f"Ones: {ones}")
print(f"Tens: {tens}")
print(f"Hundreds: {hundreds}")
print(f"Thousands: {thousands}")