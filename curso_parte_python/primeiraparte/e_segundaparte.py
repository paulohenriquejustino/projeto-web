# Curso Técnico de Informática
# Autor: Ph
# Data: 23/12/2022

# Importanto  as bibliotecas
import os
import random

# Limmpando o terminal
os.system('cls')

# Gerando números coma bliblioteca random
aleatorio = list(range(0,10))
random.shuffle(aleatorio)
print(f'Gerando números aleatórios de 1 a 10: {aleatorio}')

# Ordem ascendente
aleatorio.sort()
print(f'Ordem ascendente: {aleatorio}')

# Ordem descendente
aleatorio.reverse()
print(f'Ordem descendente: {aleatorio}')
