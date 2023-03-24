# Curso Técnico de Informática
# Autor: Ph
# Data: 09/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada 

primeiro = float(input('Digite o um número: '))
segundo = float(input('Digite um segundo número: '))

# Processo

processo = primeiro / segundo

# Saída formatada (template string)
print('-'*70)
print(f'O resultado será: {processo:.4f}')
print('='*70)