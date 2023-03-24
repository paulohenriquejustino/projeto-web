# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')


# Chamando funções
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


# Entrada de dados com estrutura de repetição while.
while(True):
   print()
   print(f'Para finalizar o progama digite 7!')
   print()
   n1 = int(input('Digite um número maior que 0 é menor que 11:  '))  
   n2 = int(input('Digite outro número maior que 0 é menor que 11:  '))
   print()
   print('1 - Soma')
   print('2 - Subtração')
   print('3 - Produto')
   print('4 - Divisão')
   print('5 - Divisão Inteira')
   print('6 - Resto da divisão')
   print('7 - Para Sair Digite 7')
   print()
   
   menu = int(input(f'Degite a operação que deseja executar entre 1 é 6:  '))
   # Condicional para finalizar o progama.
   if( n1 == 7 or n2 == 7 or menu == 7):
    break
   print()

# Criando condicionais para o meu menu
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


   
   

    