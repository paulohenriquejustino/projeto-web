# Curso Técnico de Informática
# Autor: Ph
# Data: 10/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

# Declaraçao

a = 10
b = 5
c = 'john'

# Condicional Simples
print('-'*40)
print('CONDICIONAL SIMPLES')
print('-'*40)
if (a > b):
    print('"a" é maior que "b"!')
else:
    print('"a" não é maior que "b"')
print()


# Condicional Aninhada
print('-'*40)
print('CONDICIONAL ANINHADA')
print('-'*40)
if (a < b):
    print('"a" é maior que "b"!')
elif (b != 5):
    print('"b" é diferente de "c"')
elif (c == 'john'):
    print('"c" é igual a "john"')
else:
    print('Se nada deu certo!')
print()