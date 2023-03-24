# Curso Técnico de Informática
# Autor: Ph
# Data: 16/12/2022

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declarando uma lista
listaincompleta = [1, 2, 3, 5, 6]

# Utilizando a função insert(x, y)
listaincompleta.insert(3, 4)

#Saida 
print(f'Lista incompleta:[1, 2, 3, 5, 6]')
print('-'*70)
print(f'Lista completa:{listaincompleta}')
print()