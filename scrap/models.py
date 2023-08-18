from django.db import models

# Create your models here.
print('asdfasg'.replace('a',''))

file_tres = open('file.txt','r')
print('\nlinea 36_38')
print(file_tres.closed)
file_tres.close()
print(file_tres.closed)
print('linea 36_38')
var = ' Bolsa de Viaje Universal Accesorios de | https://www.amazon.com.mx/Spardar-Organizador-Electr%C3%B3nico-electr%C3%B3nica-Auriculares/dp/B095396RMR/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=electronica&qid=1690906276&s=computers&sr=1-1 | $219.99 | FYY Organizador electr�nico, organizador de cables de viaje, bolsa de accesorios electr�nicos, funda de transporte, port�t... | 4.4 | '
var = ' Bolsa de Viaje Universal Accesorios de |'
var_2 = 'Hello World |'
with open('file.txt','r') as file:
    # print('a' in file.read())
    # print(var in file.read())
    print(var in file.read())