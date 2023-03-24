# Curso Técnico de Informática
# Autor: Ph
# Data: 16/12/2022

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaracao de variavel
soma = 0
produto1 = 0
produto2 = 0
soma_produtos = 0

# Declarando uma lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Fatiando uma lista
intervalo = lista_numeros[0:9]
segundointervalo = lista_numeros[7:13]
print(f'Número no intervalo de 1 até 9: {intervalo}')
print(f'Número no intervalo de 8 até 13: {segundointervalo}')
print('='*100)
print()

# Fatiando lista para encontrar numeros pares
pares = lista_numeros[1:14:2]
impares = lista_numeros[0:15:2]
print(f'Os números pares encontrados é: {pares}')
print(f'Os números ímpares encontrados é: {impares}')
print('='*100)
print()


# Multiplos de 2, 3 e 4
for c in range(1, 15):
    if (c % 2 == 0) and (c % 4 == 0) and (c % 3 == 0):
        print(f'Os multiplos de 2, 3, 4 é o número: {c}')
        
     
# Revertendo a lista
print('='*100)
print(f'Invertendo Lista ')
lista_numeros.reverse()
print(f'Lista invertida: {lista_numeros}')
print()

# Declarando o intervalo
intervalo1 = 5 + 6
intervalo2 = 11 + 12
soma =  intervalo1 * intervalo2
print(f'O produto dos intervalos 5-6 por 11-12 é: {soma}')

    
    



    

    
    
    
        
        
    
               
                
                     

             
        
        
                


