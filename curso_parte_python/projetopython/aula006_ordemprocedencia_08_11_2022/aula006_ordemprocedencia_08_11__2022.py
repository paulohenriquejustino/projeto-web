# Curso Técnico de Informática
# Autor: Ph
# Data: 08/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada 
nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))
nota3 = float(input('3° nota: '))
nota4 = float(input('4° nota: '))

# Operações
soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
mediacorreta = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
print(f'1° nota do aluno : {nota1}')
print(f'2° nota do aluno : {nota2}')
print(f'3° nota do aluno : {nota3}')
print(f'4° nota do aluno : {nota4}')
print(f'A soma das notas é: {soma}')
print(f'A média: {media} ERRADO!')
print(f'A média: {mediacorreta} CORRETO')
