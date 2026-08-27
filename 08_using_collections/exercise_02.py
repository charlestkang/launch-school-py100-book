# EXERCISE 2
# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins 
# with the first c.

string = "Launch School"
ind = string.find('c')
substring = string[ind: ind + 6]
print(substring)
print(len(substring))
