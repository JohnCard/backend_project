#comment
import string
from django import forms
def validate(char):
    cont = 0
    for letter in char:
        if letter not in string.ascii_letters+' ':
            cont+=1
    return cont
