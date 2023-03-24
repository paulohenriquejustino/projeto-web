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

digite = int(input(f'Digite um número milhar: '))

# Fatiando strings 

# Milhar
milhar = digite // 1000 % 10

# Centena
centena = digite // 100 % 10

# Dezena
dezena = digite // 10 % 10

# Unidade
unidade = digite // 1 % 10

# Saída
print(f'='*70)
print(f'O número na casa milhar é: {milhar}.')
print(f'O número na casa centena é: {centena}.') 
print(f'O número na casa dezena é: {dezena}.') 
print(f'O número na casa unidade é: {unidade}.') 
print(f'='*70)