# Curso Técnico de Informática
# Autor: Ph
# Data: 08/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada

primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))


# Processo

calcule = primeiro + segundo + terceiro 
multiplicacao = primeiro * segundo * terceiro


# Saída formatada (template string)

print('-'*70)
print(f'A soma dos tres números é {calcule:.0f}')
print(f'A soma dos tres números é {multiplicacao:.0f}')
print('='*70)