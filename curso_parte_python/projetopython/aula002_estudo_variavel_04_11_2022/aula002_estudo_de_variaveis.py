# Curso Técnico de Informática
# Autor: Ph
# Data: 04/11/2022
# Primeiro Progama em Python

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

# Declaraçõos
nome = 'Jonh Doe'
data_nascimento = 1970
altura = 1.77
peso = 72.5
doador = True
complexo = 3j
CONSTANTE = 10

# Saída

print('-'*70)
print('ESTUDO DE VARIÁVEIS: TIPOS')
print('='*70)
print('A variável nome é do tipo', type(nome))
print('A variável data_nascimento é do tipo',type(data_nascimento))
print('A variável altura é do tipo', type(altura))
print('A variável peso é do tipo', type(peso))
print('A variável doador é do tipo ', type(doador))
print('A variável complexo é do tipo ', type(complexo))
print('A variável CONSTANTE é do tipo ', type(CONSTANTE))

print('-'*70)

print()
print('-'*70)
print('ESTUDO DE VARIÁVEIS: SAÍDA')
print('='*70)
print('Seu nome é................... ', nome)
print('Ano de nascimento............ ',data_nascimento)
print('Você mede....................', altura,'m')
