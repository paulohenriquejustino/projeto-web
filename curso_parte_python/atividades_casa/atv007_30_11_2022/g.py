# Curso Técnico de Informática
# Autor: Ph
# Data: 30/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

n = 3
intervalo = int(input(f'Digite o final do intervalo: '))


while n<intervalo:
    mult=0
    for count in range(3,n):
        if( n % count == 0):
           mult+=1
    if (mult ==0):
           print(f'{n} é primo. ')
    n=n+2    

      

    

