# Curso Técnico de Informática
# Autor: Ph
# Data: 12/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

# Entrada

a = float(input(f'Digite o valor do primeiro segmento: '))
b = float(input(f'Digite o valor do segundo segmento: '))
c = float(input(f'Digite o valor do terceiro segmento: '))

# Operaçao (condicional)
# O if vai verificar se A é menor ou igual a 0, ou se B for menor ou igual a zero, ou se C for menor ou igual a 0.

if (a <= 0 or b <= 0 or c <= 0):
    print('='*70)
    print(f'Valor de segmento invalido.')
    print('='*70)

# O elif vai verificar o lado verdadeiro do condicional.
elif ((a  < (b + c)) and (b < (a + c)) and (c <  (b + a))):

    print('='*70)
    print(f'Forma um triângulo.')
    print('='*70)

# o else vai verificar o lado falso da condicional.    
else:
    print('='*70)
    print(f'Não forma um triângulo.')
    print('='*70)