# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Declarando 
media_altura = 0
media_peso = 0
temp = []
principal = [ ]

while(True):
    nome = str(input(f'Digite seu nome: '))
    altura = float(input(f'Digite sua altura: '))
    peso = int(input(f'Digite seu peso: '))
    codigo = int(input(f'Digite o seu código: '))

    temp.clear()
    set = {''}
    set.add(altura)
    total = sum(set)
    sair = str(input(f'Deseja continuar o progama? Digite "0" para finalizar: '))
    if sair in '0':
        break
    

print(f'Cadastro: {principal}')
total = len(principal)
print(f'Ao todo você cadastrou {total} pessoas. ')
print(total)







  








    
    


