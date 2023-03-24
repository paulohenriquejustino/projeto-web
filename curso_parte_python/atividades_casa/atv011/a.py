# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os
import copy

# Limmpando o terminal
os.system('cls')

# Declarando listas
listadenumeros = [1, 2, 3, 4, 5, 6, 7, 8, 10]

def pares():
    
    fatiandopares = listadenumeros[1:10:2]
    quantpares = len(fatiandopares)
    print(f'Os números pares encontrados na lista foi: {fatiandopares}, tem o total de {quantpares} números.')


pares() 


def impares():
    fatiandoimpares = listadenumeros[0:8:2]
    quantimpares = len(fatiandoimpares)
    print(f'Os números ímpares encontrados na lista foi: {fatiandoimpares}, tem o total de {quantimpares} números.')


impares()



    


