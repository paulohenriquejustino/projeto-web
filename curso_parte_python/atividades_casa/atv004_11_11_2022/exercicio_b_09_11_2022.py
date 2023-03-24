# Curso Técnico de Informática
# Autor: Ph
# Data: 08/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')


# Entrada
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))


# Condicional


# Maior que

if ( primeiro > segundo ):
    print('='*70)
    print(f'O {primeiro:.0f} é maior ')
    print('='*70)

elif ( primeiro > terceiro ):
    print('='*70)
    print(f'O {primeiro:.0f} é maior ')
    print('='*70)  

elif (terceiro > segundo):
    print('='*70)
    print(f'O {terceiro:.0f} é maior ')
    print('='*70)  

elif (segundo > primeiro):
    print('='*70)
    print(f'O {segundo:.0f} é maior ')
    print('='*70)  




# Menor que




if ( primeiro < segundo ):
    print('='*70)
    print(f'O {primeiro:.0f} é menor ')
    print('='*70)

elif ( primeiro < terceiro):
    print('='*70)
    print(f'O {primeiro:.0f} é menor ')
    print('='*70)   
 

elif ( terceiro < segundo):
    print('='*70)
    print(f'O {terceiro:.0f} é menor ')
    print('='*70)  


elif ( terceiro < primeiro):
    print('='*70)
    print(f'O {terceiro:.0f} é menor ')
    print('='*70)  



elif ( segundo < primeiro):
    print('='*70)
    print(f'O {segundo:.0f} é menor ')
    print('='*70)  


elif ( segundo< terceiro):
    print('='*70)
    print(f'O {segundo:.0f} é menor ')
    print('='*70)      



# Igual a 

if ( primeiro == segundo == terceiro ):
    print('='*70)
    print(f'O {primeiro:.0f} é igual {segundo} é  igual {terceiro}.')
    print('='*70)

elif ( primeiro == terceiro):
    print('='*70)
    print(f'O {primeiro:.0f} é igual {terceiro}')
    print('='*70)   
 

elif ( terceiro == segundo):
    print('='*70)
    print(f'O {terceiro:.0f} é igual {segundo} ')
    print('='*70)  


elif ( terceiro == primeiro):
    print('='*70)
    print(f'O {terceiro:.0f} é igual {primeiro}')
    print('='*70)  



elif ( segundo == primeiro):
    print('='*70)
    print(f'O {segundo:.0f} é igual {primeiro}')
    print('='*70)  


elif ( segundo == terceiro ):
    print('='*70)
    print(f'O {segundo:.0f} é igual {terceiro} ')
    print('='*70) 


