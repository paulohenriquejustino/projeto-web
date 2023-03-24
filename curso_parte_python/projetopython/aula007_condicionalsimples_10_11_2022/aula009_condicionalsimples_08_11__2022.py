# Curso Técnico de Informática
# Autor: Ph
# Data: 10/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

a = 10
b = 5
c = 'José'
d = 'josé'

print('-'*40)
print('ESTUDO DE CONDICIONAIS: OPERADORES RELACIONAIS')
print()

# Operador == (igualdade)
if (c ==d):
    print('-'*40)
    print(f'{c} é igual a {d}')
    print('-'*40)
else:
    print(f'{c} não é igual a {d}')

# Operador != (diferença)
if (a != c):
    print('-'*40)
    print(f'{a} é diferente a {c}')
    print('-'*40)
else:
    print(f'{a} não é diferente a {c}')

# Operador > (maior que)
if ( a > b):
    print('-'*40)
    print(f'{a} é maior que {b}')
    print('-'*40)
else:
    print(f'{b} não é menor que {a}')

# Operador >= (maior ou igual)
if (a >= b):
    print('-'*40)
    print(f'{a} é maior ou igual que {b}')
    print('-'*40)
else:
    print(f'{a} não é maior ou igual a {b}')

# Operador <= (menor ou igual)
if (b <= a):
    print('-'*40)
    print(f'{a} é menor ou igual que {a}')
    print('-'*40)
else:
    print(f'{b} não é menor ou igual a {a}')
    
