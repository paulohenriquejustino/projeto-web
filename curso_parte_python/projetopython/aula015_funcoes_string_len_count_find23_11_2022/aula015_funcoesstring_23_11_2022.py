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


quantidade_caracteres = len(variavel_str)
ocorrencia_caracteres = variavel_str.count('s', 0, 10)
posicao_caractere = variavel_str.find('Python!')

print(f'String: {variavel_str}')
print(f'Quantidade de caracteres: {quantidade_caracteres}')
print(f'Ocorrência de "s" na String: {ocorrencia_caracteres} ocorrências')
print(f'Índice de Palavra "Python!": Posição {posicao_caractere}')
print('-'*70)