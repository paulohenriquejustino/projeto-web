# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Criando uma função
def dados():
   # transformando as variaveis em global
   global n1
   global n2
   global menu
   n1 = int(input('Digite um número maior que 0 é menor que 11:  '))
   n2 = int(input('Digite outro número maior que 0 é menor que 11:  '))
   print()
   print(f'1 - Soma')
   print(f'2 - Subtração')
   print(f'3 - Produto')
   print(f'4 - Divisão')
   print(f'5 - Divisão Inteira')
   print(f'6 - Resto da divisão')
   print(f'7 - Digitar novos números')
   print()
   menu = int(input(f'Degite a operação que deseja executar entre 1 é 7:  '))
# Invocando função
dados()  
print()

# Criando funções    
def soma():
    soma = n1 + n2
    print(f'A soma de {n1} + {n2} = {soma}')


def subtracao():
    diminuir = n1 -  n2
    print(f'A subtração de {n1} + {n2} = {diminuir}')


def produto():
    prod = n1 * n2
    print(f'O produto de {n1} * {n2} = {prod}')


def  divisao():
    div = n1 / n2
    print(f'A divisão de {n1} / {n2} = {div:.3f}')


def divisaointeira():
    inteira = n1 // n2
    print(f'A divisão inteira de {n1} // {n2} = {inteira}')


def restodadivisao():
    resto  = n1 % n2
    print(f'O resto da divisão entre {n1} por {n2} = {resto}')


def voltar():
    return dados()

# Criando condicionais para menu
if (menu == 1):
    soma()


elif(menu == 2):
    subtracao()
    

elif(menu == 3):
    produto()


elif(menu == 4):
    divisao()


elif(menu == 5):
    divisaointeira()


elif(menu == 6):
    restodadivisao()


elif(menu == 7): 
    voltar()
   

    