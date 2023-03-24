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
variavel_str = "Estou estudando Python!"
lista = ['Olá', 'Mundo'] 

separando_caracteres = variavel_str.split()
juntar_string = ' '.join(lista)
frase_com_espacos = '   Olá mundo!   '
frase_sem_espacos = frase_com_espacos.strip()

print(f'String: {variavel_str}')
print(f'Palavras sepradas, "Gera uma  [lista]": {separando_caracteres} ')
print(f'Antes: {lista} -- Depois: {juntar_string}')
print('-'*70)
print(f'{frase_com_espacos}')
print(f'Quantidade de caracteres na frase com espaços: {len(frase_com_espacos)}')
print(f'Quantidade de caracteres na frase sem espaços: {len(frase_sem_espacos)}')