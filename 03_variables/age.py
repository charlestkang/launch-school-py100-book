# EXERCISE 6

age = int(input())

def prediction(age, offset):
    print(f"In {offset} years, you will be {age + offset} years old.")

for i in range(4):
    prediction(age, 10 * (i + 1)) 
