# Curso Técnico de Informática
# Autor: Ph
# Data: 25/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Entrada de dados
digite = str(input(f'Digite um nome: ')).lower()
# Usando Slice
inversao = digite[::-1]

# Condicional
if (digite == inversao):
    print(f'O inverso de {digite} é {inversao}')
    print('-'*70)
    print(f'A palavra e um palíndromo')
else:
    print(f'O inverso de {digite} é {inversao}')
    print('-'*70)
    print(f'A palavra digitada não e um palíndromo.')    
