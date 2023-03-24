# Curso Técnico de Informática
# Autor: Ph
# Data: 30/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaraçao

cont = 0

# Entrada de dados
primeiro = int(input("Digite o primeiro número do intervalo: "))
ultimo = int(input("Digite o último número do intervalo: "))
ignorarprimeiro= int(input("Digite o primeiro número que deseja excluir: "))
ignorarsegundo = int(input("Digite o segundo número que deseja excluir: "))
ignorarterceiro = int(input("Digite o terceiro número que deseja excluir: "))

# Usando for
for cont in range(primeiro, ultimo):
    # Usando not para forçar os números e serem falsos.
    if cont not in (ignorarprimeiro,ignorarsegundo,ignorarterceiro):
        print(f'{cont}')
    else:
        print('Número ignorado')