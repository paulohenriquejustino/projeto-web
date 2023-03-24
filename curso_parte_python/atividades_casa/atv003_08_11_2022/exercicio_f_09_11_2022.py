# Curso Técnico de Informática
# Autor: Ph
# Data: 09/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada 

primeiro = float(input('Digite um número e descubra seu dobro e triplo: '))
segundo = float(input('Digite o segundo número: '))




# Calculo
soma1 = primeiro * 2
soma2 = primeiro * 3
soma3 = segundo * 3
soma4 =  segundo * 3

# Saída formatada (template string)

print('='*70)
print(f'O dobro do primeiro número digitado é: {soma1} o seu triplo é: {soma2}')
print(f'O dobro do segundo número digitado é: {soma3} o seu triplo é: {soma4}')
print('='*70)
