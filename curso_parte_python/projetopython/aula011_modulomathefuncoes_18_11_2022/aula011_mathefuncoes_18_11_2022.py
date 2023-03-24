# Curso Técnico de Informática
# Autor: Ph
# Data: 18/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os
import math
# Limmpando o terminal

os.system('cls')

print('-'*50)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('-'*50)
print()

# Declarações
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5
ca = 10

# Cálculo
potencia = math.pow(base, expoente)
raizquadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co,ca)


# Saída
print('='*70)
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizquadrada}')
print(f'O seno de {angulo} é: {seno}')
print(f'O cosseno de {angulo} é: {cosseno}')
print(f'O seno de {angulo} é: {tangente}')
print(f'O valor da hipotenusa é: {hipotenusa}')
print('='*70)