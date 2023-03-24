# Curso Técnico de Informática
# Autor: Ph
# Data: 04/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Uso do comando Input


# Entrada

nome = str(input('Qual o seu nome: '))
datanascimento = int(input('Em que ano você nasceu: '))
altura = float(input('Qual a sua altura: '))
peso = float(input('Quanto você pesa: '))


#Saída
print('-'*70)
print('ESTUDO DE ENTRADA DE DADOS COM INPUT')
print('='*70)
print('Seu nome é..................', nome)
print('Ano de nascimento...........', datanascimento)
print('Você mede....................', altura, 'm')
print('Seu peso é....................', peso, 'Kg')
print('='*70)
print('Fim do Progama!')
print('-'*70)

