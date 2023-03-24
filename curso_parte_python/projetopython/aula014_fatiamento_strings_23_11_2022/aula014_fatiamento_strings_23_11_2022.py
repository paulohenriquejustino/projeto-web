# Curso Técnico de Informática
# Autor: Ph
# Data: 23/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

frase = 'String em Python!'
texto = 'String em Python!'

print(f'Imprimindo a variável "frase": {frase}')
print(f'Imprimindo a variável "texto": {texto}')

char_posicao_0 = frase[0]
char_posicao_10 = frase[10]
chars_0_a_10 = frase[0:10]
char_0_a_10_com_intervalo_2 = texto[0:10:2]


print(f'Imprimindo o char na posição 0: {char_posicao_0}')
print(f'Imprimindo o char na posição 10: {char_posicao_10}')
print(f'Imprimindo os chars de 0 a 10: {chars_0_a_10}')
print(f'Imprimindo os chars de 0 a 10 com intervalo 2: {char_0_a_10_com_intervalo_2}')