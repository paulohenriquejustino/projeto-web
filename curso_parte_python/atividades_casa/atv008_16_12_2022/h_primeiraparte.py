# Curso Técnico de Informática
# Autor: Ph
# Data: 23/12/2022

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Declaração 
soma = 0 
listadenotas = []
notas_somadas = 0
media = 0

while(True):
    notas = int(input(f'Digite o valor da nota: '))
    listadenotas.append(notas)
    soma = soma + notas
    media = soma / 3

    
    
    if (notas == 's') or (notas == 0):
        del listadenotas[-1]
        contando_notas = len(listadenotas)
        print(f'A quantidade de notas digitadas é: {contando_notas}')
        print(f'As notas digitas na ordem : {listadenotas}')
        listadenotas.reverse()
        print(f'Lista na ordem inversa: {listadenotas}', end=' ')
        print(f'A soma das notas é: {soma}')
        
        print(f'A média das notas é: {media:.2f}')
        break



 