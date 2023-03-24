# Curso Técnico de Informática
# Autor: Ph
# Data: 12/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

# Entrada
# Usei int, por que velocidade nao pode ser um ponto flutuante.
velocidade = int(input('Digite a velocidade que o carro passou no radar: '))


# Cálculos (condicional)
# O if vai testar se a velocidade é menor que 60.
if ( velocidade <= 60 ):
    print('='*70)
    print(f'Velocidade Normal')
    print('='*70)

# o else vai funcionar caso o bloco acima for falso.  
else:
    print('='*70)
    print(f'Limite de velocidade acima do permitido')    
    print('='*70)
