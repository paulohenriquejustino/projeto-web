# Curso Técnico de Informática
# Autor: Ph
# Data: 10/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Declaração 

a =  10
b = 5
c = 'john'

print('-'*40)
print('ESTUDO DE CONDICIONAIS: OPERADORES LÓDIGCOS: ')
print('-'*40)
print()



# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print()    


# E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print()


# Ou ( or ) VERDADEIRO
print('OU (or) VERDADEIRO ')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')  

print()    

# OU (or ) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'Jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')