# Curso Técnico de Informática
# Autor: Ph
# Data: 12/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

# Entrada

ano = int(input('Digite um ano: '))


# Operaçao

# O if vai testar se o ano e divisivel por 4 com resto 0 e tambem por 400 com resto diferente ou igual a zero, ou se ano e divisivil por 400 com resto 0.
if (ano&4==0 and ano%100 != 0) or (ano%400==0):
    print('='*70)
    print(f'O ano e bissexto.')
    print('='*70)
    
# o else vai funcionar caso o bloco acima for falso.      
else:
    print('='*70)
    print(f'Não e bissexto.')
    print('='*70)    