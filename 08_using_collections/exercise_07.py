# EXERCISE 7
# Write Python code to replace all the : characters in the string below with +.

# Copy Code
# info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# Try this problem using the methods you've learned about in this chapter. Once 
# you have that working, use the Python documentation for the str type to find 
# an alternative solution.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info)

# Before checking Python documentation
new_info = "".join([char if char != ":" else "+" for char in info])
print(new_info)

# After checking Python documentation
new_info = info.replace(":", "+")
print(new_info)

# Book implementation pre-documentation
new_info = "+".join(info.split(":"))
print(new_info)
