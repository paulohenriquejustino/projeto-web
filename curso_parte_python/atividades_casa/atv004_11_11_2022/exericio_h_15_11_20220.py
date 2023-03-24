# Curso Técnico de Informática
# Autor: Ph
# Data: 12/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')



# declaraçoes

a = int(input(f'Digite valor de A: '))
b = int(input(f'Digite valor de B: '))
c = int(input(f'Digite valor de C: '))
# Calculo


# vai verificar se a ou b e igual a zero.
if ( a == 0 or b == 0):
   (print(f'Valor incorreto.'))

# esse bloco vai funcionar caso o acima for falso.
else:
    #Calculando o delta
    delta = (b**2-4*a*c)
    #Encontrando valor da equação. 
    x1 = (-b + (delta**(0.5))) / 2*a
    x2 = (-b - (delta**(0.5))) / 2*a

print('='*70)
print(f'O resultado é {x1}')
print(f'O resultado é {x2}')
print('='*70)
