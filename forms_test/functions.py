#comment
import string
from django import forms
def validate(char):
    cont = 0
    for letter in char:
        if letter not in string.ascii_letters+' ':
            cont+=1
    return cont

def validate_email(email):
    characters_email = '()<>,;:"[]ç%& '
    cont = 0
    for char in email:
        if char in characters_email:
            cont +=1
    return cont
