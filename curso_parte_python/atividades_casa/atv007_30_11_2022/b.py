# Curso Técnico de Informática
# Autor: Ph
# Data: 30/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Entrada de dados


inicio = int(input(f'Digite o inicio do intervalo:  '))
print('='*102)
print('\033[31m'+'Atenção antes de digitar o final do intervalo, lembre que o número digitado vai ser diminuido por "-1"'+'\033[0;0m')
print(f'='*102)
fim = int(input(f'Digite o final do intervalo: '))
print(f'-'*102)
passo = int(input(f'Digite a contagem do intervaldo:  '))

# Imprimindo 

for numero in range(inicio, fim, passo):
    print(f'-'*102)
    print(f'O {numero} está dentro do intervalo.')
    