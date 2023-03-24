# Curso Técnico de Informática
# Autor: Ph
# Data: 08/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')



# Entrada 

seunascimento = int(input('Qual é seu ano de nascimento: '))


# Processo
idade = seunascimento - 2022 
soma = idade * -1 

# Saída formatada (template string)
print('-'*70)
print(f'Sua idade é {soma}')
print('='*70)



