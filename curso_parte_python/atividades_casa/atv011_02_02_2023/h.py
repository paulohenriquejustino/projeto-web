# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os
from statistics import mean

# Limmpando o terminal
os.system('cls')

# Criando uma função
def  dados():
    global media_pesos
    global media_altura
    media_altura = 0
    media_pesos = 0
    temp = []
    principal = [ ]
    lista_pesos = []
    lista_altura = []

    # Criando uma estrutura de repetição while para fazer o cadastro dos clientes.
    while(True):
        global nome
        global codigo
        global altura
        global peso
        print(f'CADASTRO DO CLIENTE')
        print()
        nome = str(input(f'Digite seu nome: '))
        altura = float(input(f'Digite sua altura com ponto : '))
        peso = int(input(f'Digite seu peso: '))
        codigo = int(input(f'Digite o seu código: '))
        temp.append(nome)
        temp.append(peso)
        temp.append(altura)
        temp.append(codigo)
        lista_pesos.append(peso)
        lista_altura.append(altura)
        # Utilizando mean para calcular a média de peso e altura, que foi guardado dentro de uma lista.
        media_pesos = mean(lista_pesos)
        media_altura =  mean(lista_altura)
        # Adicioando todos os dados digitado na minha lista principal. [:] = percorre do inicio até o fim da lista.
        principal.append(temp[:])
        temp.clear()
        
        sair = str(input(f'Deseja continuar o progama? Digite "0" para finalizar: '))
        if sair in '0':
            break
        else:
            continue
   
# invocando a função dados para fazer o cadastro.
dados()

# Criando uma função para mostra a tabela formatada.
def tabela():
    cadastrados = []
    usuarios = {'Código': codigo, 'Nome': nome, 'Altura': altura, 'Peso': peso}
    cadastrados.append(usuarios)
    print("PROGAMA ACADEMIA:")
    print('-'*70)
    # Utilizando .ljust para mover os dados para uma posiçao desejada.
    print('Código'.ljust(20), 'Nome'.ljust(20), 'Altura'.ljust(20), 'Peso'.ljust(20))
    print('='*70)
    # Fazendo uma varredura no meu dicionario buscando dados dos clientes cadastrados que esta em uma lista.
    for usuarios in cadastrados:
                print(f'{usuarios["Código"]}'.ljust(20), f'{usuarios["Nome"]}'.ljust(20), f'{usuarios["Altura"]}'.ljust(20),
                            f'{usuarios["Peso"]}'.ljust(20))
    print('-'*70)
    print('Média:'.ljust(40), f'{media_altura:.2f}'.ljust(20), f'{media_pesos}')
    print('='*70)

# Invocando a função para mostrar a tabela.
tabela()








  








    
    


