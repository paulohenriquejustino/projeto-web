# Curso Técnico de Informática
# Autor: Ph
# Data: 27/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaração

resposta = ' '


# Entrada de dados

# Validação de dados usando lower() para jogar todas as letras para minuscula.

nome = str(input(f'Digite o nome do aluno: ')).lower()

# Usandos funções

# rfind() esse vai fazer a mesma função do find, porem começando do lado direito para o esquerdo.

ocorrencia = nome.count('o')
procurandoinicio = nome.find('o') 
procurandofinal = nome.rfind('o')

# Saída
print(f'='*70)
print(f'A quantidade de letra "o" no nome é: {ocorrencia}  ')
print(f'A primeira letra "o" aparece na posição: {procurandoinicio}')
print(f'A ultima  letra "o" aparece na posição: {procurandofinal}')
print(f'='*70)