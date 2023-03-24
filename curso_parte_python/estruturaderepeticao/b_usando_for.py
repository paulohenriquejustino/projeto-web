# Curso Técnico de Informática
# Autor: Ph
# Data: 04/12/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaração 

respotas = ' '
nome = 0
senha = 0
chance = 0

# Flag

cont = 0

# Estrutura for

for cont in range(0,3):
    print(f'Voce tem apenas 3 TENTATIVAS!')
    print()
    nome = str(input(f'Digite o seu nome: '))
    senha = str(input(f'Digite a sua senha: '))
    if ( nome == senha ):
        print(f'Por favor digite uma senha diferente do seu nome!')
    else:
        print(f'Pronto, nome e senha correto!')
        break       