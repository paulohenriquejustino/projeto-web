# Curso Técnico de Informática
# Autor: Ph
# Data: 08/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
nota3 = float(input('Digite a 3° nota: '))
nota4 = float(input('Digit a 4° nota: '))


# Processo(calculo)

media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída formatada (template string)


print('-'*70)
print(f'A média do aluno será: {media} ')
print('='*70)


