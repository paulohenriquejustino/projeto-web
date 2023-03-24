# Curso Técnico de Informática
# Autor: Ph
# Data: 23/12/2022

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Declaraçao
maior = 0
menor= 0

# Criando uma lista 
listadenumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior = max(listadenumeros)
menor = min(listadenumeros)
print(f'Lista declarada: {listadenumeros}')
print(f'O maior número dentro da lista é {maior}, o menor {menor}.')