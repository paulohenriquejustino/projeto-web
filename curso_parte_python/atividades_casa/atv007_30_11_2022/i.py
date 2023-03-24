# Curso Técnico de Informática
# Autor: Ph
# Data: 30/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Usando while

letra = ' '
while letra != 'f':
    print('estou em loop')
    letra = str(input('Digite uma letra para sair: ')).lower()
else:
 print(f'Fim!')