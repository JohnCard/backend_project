import string

# function to validate a name within a user form \\ error: returns a number bigger than 0 \\ well done: returns a 0
def validate(char):
    cont = 0
    for letter in char:
        if letter not in string.ascii_letters + ' ':
            cont += 1
    return cont
