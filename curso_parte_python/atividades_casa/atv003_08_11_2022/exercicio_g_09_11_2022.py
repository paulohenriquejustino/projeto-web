# Curso Técnico de Informática
# Autor: Ph
# Data: 09/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada 

primeiro = float(input('Digite um número em metros  para  converter em centimetros e milimetros: '))

# Calculo

metroparacentrimetros = primeiro * 100
centimetrosparamilimetros = metroparacentrimetros / 10

# Saída formatada (template string)

print('='*70)
print(f'O valor em centimetros será: {metroparacentrimetros:.2f}')
print(f'O valor convertido de centimetros para milimetros será: {centimetrosparamilimetros:.2f}')
print('='*70)


