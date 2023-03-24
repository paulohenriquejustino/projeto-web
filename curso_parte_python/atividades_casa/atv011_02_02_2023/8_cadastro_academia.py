# Curso Técnico Em Informática
# Autor: Renan Ferreira Nunes
# Data: 04/02/2023

# Importando bibliotecas
import os
from time import sleep

# Limpando a tela
os.system('cls')

# Funções
def firula():
    sleep(0.3)
    os.system('cls')


def cabecalho():
    print('-'*70)
    print('SISTEMA MAROMBA FITNESS')
    print('='*70)
    print()


def cadastra_usuario():
    clientes = []

    cabecalho()
    
    # O while vai rodar até o usuário digitar o número 0
    while True:

        # Entrada de dados
        codigo = str(input('Digite seu código de matrícula: '))
        nome = str(input('Digite o seu nome: '))
        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite o seu peso: '))

        # Criando um dicionário e colocando as informações que o usuário digitar em suas respectivas chaves
        cliente = {'Código': codigo, 'Nome': nome, 'Altura': altura, 'Peso': peso}
        clientes.append(cliente) # Adicionando esse dicionário na lista clientes que declarei no inicio

        firula()
        cabecalho()

        print(f'Usuário {nome} cadastrado!\n')
        continuar = int(input('Deseja sair? [0]: '))

        firula()
        cabecalho()

        # Condicional que irá quebrar o meu laço
        if continuar == 0:
            # Inicializando minhas variáveis
            altura_total = 0 
            peso_total = 0

            # Um for para somar a altura e peso de todos os clientes
            for cliente in clientes:
                altura_total += cliente['Altura']
                peso_total += cliente['Peso']
            
            # Duas variáveis pra descobrir a média de altura e peso
            # Usando o len para descobrir quantos clientes existem na minha lista
            # Assim podendo fazer a divisão
            med_altura = altura_total / len(clientes)
            med_peso = peso_total / len(clientes)

            # O ljust() serve pra alinhar as strings 
            print("Tabela de clientes:\n")
            print('-'*70)
            print('Código'.ljust(20), 'Nome'.ljust(20), 'Altura'.ljust(20), 'Peso'.ljust(20))
            print('='*70)

            # Pra cada cliente da minha lista, os valores serão formatados com o ljust
            # Fazendo com que a minha tabela fique alinhada
            for cliente in clientes:
                print(f'{cliente["Código"]}'.ljust(20), f'{cliente["Nome"]}'.ljust(20), f'{cliente["Altura"]}'.ljust(20),
                            f'{cliente["Peso"]}'.ljust(20))

            # Aqui a média será mostrada logo abaixo utilizando o ljust para alinhar
            print('-'*70)
            print('Média:'.ljust(40), f'{med_altura}'.ljust(20), f'{med_peso}')
            print('='*70)
            

            break
            
        else:
            pass

cadastra_usuario()
