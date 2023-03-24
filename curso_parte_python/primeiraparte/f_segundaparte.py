# Curso Técnico de Informática
# Autor: Ph
# Data: 23/12/2022

# Importanto  as bibliotecas
import os
import random

# Criando uma lista
listamega = []
listaloto = []

# Iniciando contador para controle
i = 0
f = 0

#Loop para gerar 10 números
while i < 10:
    listamega.append(random.randint(1,60))
    i = i + 1
    while f < 18:
        listaloto.append(random.randint(1,60))
        f = f + 1

# Saída
print(f'Números gerados da mega sena:{listamega}')
print(f'Números gerados da lotofacil:{listaloto}')
