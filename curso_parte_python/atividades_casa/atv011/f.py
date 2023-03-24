# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')
# Chamando uma função


def listas():
    primeiralist = ['Nome', 'Peso', 'Idade']
    segundalist = ['Paulo', '40', '18']
    dicionario = {}
    for chave, valor in zip(primeiralist, segundalist):
        dicionario[chave] = valor
        print(f'{chave}: {valor}')


# invocando a função
listas()





