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
    segundalist = ['John', '40', '1.8']
    dicionario = {}
    # Utilizando a função zip para retornar elementos da mesma posição em listas diferentes.
    for i, j in zip(primeiralist, segundalist):
        print()
        dicionario[i] = j
        print(dicionario)


# invocando a função
listas()





