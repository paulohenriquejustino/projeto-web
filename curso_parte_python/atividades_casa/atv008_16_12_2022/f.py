# Curso Técnico de Informática
# Autor: Ph
# Data: 23/12/2022

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Declarando uma lista
listadosnomes = []

# Usando for 
for c in range(0, 5):
    nome = str(input(f'Digite um nome: '))
    listadosnomes.append(nome)
    for indece, nome in enumerate(listadosnomes):
        print('-'*70)
        print(f'{nome} esta no índice: {indece}')
    
   
   





