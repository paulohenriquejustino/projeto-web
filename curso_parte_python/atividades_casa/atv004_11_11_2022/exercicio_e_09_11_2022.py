# Curso Técnico de Informática
# Autor: Ph
# Data: 12/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

# Entrada

distanciaviagem = float(input(f'Qual foi a distancia em km da viagem: '))

# Calculos
# O IF vai testar se a distancia for menor que 200km.
if ( distanciaviagem <= 200 ):
    soma = distanciaviagem * 0.70
    print('='*70)
    print(f'O preço da passagem será {soma:.0f} reais.')
    print('='*70)

# O else vai testa caso o bloco acima for falso.    
else:
    ( distanciaviagem >= 200 )
    soma2 = distanciaviagem * 0.40
    print('='*70)
    print(f'O preço da passagem será {soma2:.0f} reais.')
    print('='*70)
