# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')


# Declaração
contagem_de_acertos = []
contagem = 0
continuar = 0


# Funções para verificar as respostas digitadas.
def mg():
    if minas != 'Belo horizonte':
        print('\033[31m'+'Você errou, tente novamente.'+'\033[0;0m')
        
    else:
        print('\033[32m'+'Você acertou, ganhou um ponto.'+'\033[0;0m')
        # Caso a respotas esteja digitada corretamente, ira adicionar dentro de uma lista para depois fazer a contagem.
        contagem_de_acertos.append(minas)


def ac():
    if acre != 'Rio branco':
        print('\033[31m'+'Você errou, tente novamente.'+'\033[0;0m')
        
    else:
        print('\033[32m'+'Você acertou, ganhou um ponto.'+'\033[0;0m')
        # Caso a respotas esteja digitada corretamente, ira adicionar dentro de uma lista para depois fazer a contagem.
        contagem_de_acertos.append(acre)


def am():
    if amazonas != 'Manaus':
        print('\033[31m'+'Você errou, tente novamente.'+'\033[0;0m')
        
    else:
        print('\033[32m'+'Você acertou, ganhou um ponto.'+'\033[0;0m')
        # Caso a respotas esteja digitada corretamente, ira adicionar dentro de uma lista para depois fazer a contagem.
        contagem_de_acertos.append(amazonas)


def ce():
    if ceara != 'Fortaleza':
        print('\033[31m'+'Você errou, tente novamente.'+'\033[0;0m')
        
    else:
        print('\033[32m'+'Você acertou, ganhou um ponto.'+'\033[0;0m')
        # Caso a respotas esteja digitada corretamente, ira adicionar dentro de uma lista para depois fazer a contagem.
        contagem_de_acertos.append(ceara)

def dicas():
    print('\033[33m'+'Digite o nome da capital com APENAS a primeira letra MAIUSCULA!'+'\033[0;0m')       


# Progama Principal 
# Utilizando estrutura de repetição while para fazer as perguntas.
while(True):
    dicas()
    print()
    minas =  input(f'Qual é a capital de Minas Gerais? ') # Belo Horizonte
    print()
    acre =  input(f'Qual é a capital do Acre? ') # Rio branco
    print()
    amazonas =  input(f'Qual é a capital do Amazonas? ') # Manaus
    print()
    ceara =  input(f'Qual é a capital dO Ceará? ') # Fortaleza
    print()
    # Invocando as funções
    mg()


    ac()


    am()


    ce()

    # Utilizando o len para contar os acertos.
    contagem = len(contagem_de_acertos)
    print()
    print(f'Você acertou no total {contagem} perguntas!')
    continuar = input(f'Deseja finalziar o progama? ')
    print()
    if (continuar in 'Sim' or continuar in 'sim'):
        break
    
    
