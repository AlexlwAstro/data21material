

"""
If you actually make a function like this, there's
something wrong with you!
"""


def print_function(some_variable):
    print(some_variable)
    return some_variable


"""
Don't. Just ... don't!
"""
def print(isalpha):
    return isalpha + 1
isalpha = 1
print(print(isalpha))
"""
Note that you can no longer print anything in the terminal!!!
"""