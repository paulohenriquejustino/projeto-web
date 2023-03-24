# Curso Técnico de Informática
# Autor: Ph
# Data: 04/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaração 

respotas = ' '
digite = 0


# Entrada de dados

while (True):
    digite = int(input(f'Digite uma nota de 0 até 10: '))

    if (digite < 0 or digite > 10):
        print(f'Digite um valor válido!')

    else: 
       print(f'{digite} é um valor válido. ')
    break
   

