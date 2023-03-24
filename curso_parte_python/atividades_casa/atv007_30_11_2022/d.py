# Curso Técnico de Informática
# Autor: Ph
# Data: 30/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaracao 

resposta = ' '
inicio = 0
final =  101
passo = 1


# Usando for

for numero in range(inicio, final, passo):
    if ( numero % 2 == 0): # calculando número pares.
    
     print(f'{numero}',end="," )
     

