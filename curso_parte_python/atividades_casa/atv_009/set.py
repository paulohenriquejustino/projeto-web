# Curso Técnico de Informática
# Autor: Ph
# Data: 30/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaração
set = {''}
set2= {''}
nomes = 0

print(f'Nomes repetidos ira aparecer apenas uma vez!.')
print()
# Usando for
for c in range(0,2):
    nome = str(input(f'Digite nome para ser adicionado no set: '))
    set.add(nome)
    set.discard('')
    print()
    
print(f'Você adicionou no set1 os nomes: {set}')
print('-'*70)

remover = str(input(f'Deseja remover algum nome do set? '))
if (remover == 'sim') or (remover == 'Sim'):
    set.discard(str(input(f'Digite o nome que deseja remover do set: ')))
    print(f'Seu novo set: {set}')
    print('-'*70)
          
else:
    pass

set2.discard('')
unir = str(input(f'Deseja unir um set1 ao set2? '))
print()
if (unir == 'sim') or (unir == 'Sim'):
    fazendounir = set.union(set2)
    print(f'Os sets unidos: {fazendounir}')
if (unir == 'nao') or (unir == 'Não'):
    pass

            
        
            

         



         

    
