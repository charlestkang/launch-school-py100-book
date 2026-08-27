# EXERCISE 6

# Write a function that takes a string as an argument and returns an all-caps version of the string 
# when the string is longer than 10 characters. Otherwise, it should return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def conditional_upper(s):
    return (s.upper() if len(s) > 10 else s)

# Testing

s = input("Prompt to selectively uppercase if longer than 10 chars:\n")
print(conditional_upper(s))
