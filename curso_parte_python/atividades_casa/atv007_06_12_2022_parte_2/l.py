# Curso Técnico de Informática
# Autor: Ph
# Data: 07/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Entrada 
loginsalvo = str(input(f'Crie seu login: '))
senhasalva = str(input(f'Crie sua senha: '))

# Entrada
while(True):
    login = str(input(f'Digite seu login: '))
    senha = str(input(f'Digite sua senha: '))
    # Condicional
    if ( login == loginsalvo and senha == senhasalva):
        print('\033[32m'+'Login correto'+'\033[0;0m')
        break
    else:
        print('\033[31m'+'Login incorreto'+'\033[0;0m')
        print('\033[33m'+'Digite o login é senha criados.'+'\033[0;0m') 
        
 

   





        
 
         

