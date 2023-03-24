# Curso Técnico de Informática
# Autor: Ph
# Data: 23/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

print('Trabalhando com Strings: Funções')
print('='*70)

# Declaração
variavel_str = 'Estou estudando Python!'

resultado_do_replace = variavel_str.replace('Python', 'Java')

if ('estudando' in variavel_str):
    resposta = "verdadeiro"
else:
    resposta = "Falso"    

print(f'String original: {variavel_str}') 
print(f'Quantidade de caracteres: {resultado_do_replace}') 
print(f'Exista a palavra "estudando" na string " {variavel_str}": {resposta}')
print('-'*80)
