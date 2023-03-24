# Curso Técnico de Informática
# Autor: Ph
# Data: 25/11/2022


# Entrada de dados.
nome = str(input('Digite seu nome:'))

# Nome com todas letras maisculuas.

maisculas = nome.upper()

# Nome com todas letras minusculas.

minuscula = nome.lower()

# Quantas letras tem sem considerar o espaco.

semespaco = len(nome) - nome.count(' ')

# Quantas letras tem o seu primeiro nome

primeironome = nome.find(' ')


# Saida de dados
print('Analizando o nome...')
print(f'Seu nome em letras maisculas e: {maisculas}')
print(f'Seu nome em letras minusculas e: {minuscula}')
print(f'Seu nome sem espaco contem: {semespaco}')
print((f'Seu primeiro nome e: {primeironome}'))