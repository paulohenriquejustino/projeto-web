# Curso Técnico de Informática
# Autor: Ph
# Data: 16/12/2022

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaracao
soma = 0
numero = 0
lista = []

# Criando lista com 5 numeros usando for
for c in range(0, 5):
    numero = int(input(f'Digite um número inteiro: '))
    lista.append(numero)
    soma = soma + numero
print(f'A soma dos números digitados é: {soma}')  

   
    
    


