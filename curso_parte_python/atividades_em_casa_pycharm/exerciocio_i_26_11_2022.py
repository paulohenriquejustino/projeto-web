# Curso Técnico de Informática
# Autor: Ph
# Data: 27/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaração

resposta = ' '


# Entrada de dados

nome = str(input(f'Digite seu nome completo: '))


# Usando função Split para separar os nomes.

dividindo = nome.split()

# Fatiando strings
# Obs: o uso do -1 e para pega sempre o ultimo nome da lista(seguindo da direita para esquerda).

# Ex: ['Paulo', 'henrique', 'de', 'paiva', barbosa'', 'justino']


primeironome = dividindo[0]
ultimonome = dividindo[-1]

# Saída

print(f'Seu primeiro nome é: {primeironome}')
print(f'Seu ultimo nome é: {ultimonome}')
