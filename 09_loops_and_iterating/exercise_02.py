# EXERCISE 2
# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code
# should use a for loop to display the future ages.

# NOTE: I already used a for loop in the Input/Output chapter; no change was necessary.

age = int(input("How old are you? "))
print()
print(f"You are {age} years old.")
for i in range(4):
    print(f"In {(i + 1) * 10} years you will be {age + ((i + 1) * 10)} years old.")
