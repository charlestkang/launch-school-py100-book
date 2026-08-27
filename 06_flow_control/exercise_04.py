# EXERCISE 4
# Refactor this code to use a regular if statement instead.

# Copy Code
# def baz():
#     return ('bar' if foo() else qux())

def baz():
    if foo():
        return 'bar'
    else:
        return qux()
