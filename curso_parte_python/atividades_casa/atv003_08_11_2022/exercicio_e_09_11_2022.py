# Curso Técnico de Informática
# Autor: Ph
# Data: 09/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada 

primeiro = int(input('Digite um número e descubra o sucessor e antecessor: '))


# Processo 

soma1 = primeiro - 1
soma2 = primeiro + 1


# Saída formatada (template string)

print('='*70)
print(f'O antecessor será: {soma1}, o sucessor {soma2}')
print('='*70)