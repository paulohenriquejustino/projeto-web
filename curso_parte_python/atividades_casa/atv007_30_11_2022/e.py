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
soma = 0
cont = 0
numero = 0

# Usando for

for numero in range(1, 100):
    if ( numero % 2 == 0): # calculando número pares.
        soma += numero
        

    print(f'A soma dos pares foi {soma} ')
  
       
     
