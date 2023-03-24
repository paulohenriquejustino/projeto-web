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
    print(f'O inverso de {digite} e {inversao}')
    print(f'A palavra e um palindromo')
else:
    print(f'A palavra digitada nao e um palindromo.')    
