age = int(input("How old are you? "))
print()
print(f"You are {age} years old.")
for i in range(4):
    print(f"In {(i + 1) * 10} years you will be {age + ((i + 1) * 10)} years old.")
