# Curso Técnico de Informática
# Autor: Ph
# Data: 10/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


print('-'*50)
print('Prática: verificando valor quebrado')
print('-'*50)


# Entrada de dados

valor = float(input('Digite um valor com casas decimais: '))


# Condicional

if (valor % 1 == 0):
    print(f'Valor {valor} inválido! O número digitando é inteiro')
else: 
    print()
    print(f'O valor ditado foi {valor}, entrada correta')


print('-'*50)
print('Fim do progamada')
print('-'*50)
         