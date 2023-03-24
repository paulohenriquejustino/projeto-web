# Curso Técnico de Informática
# Autor: Ph
# Data: 19/12/2022

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declarando uma lista
listadevogais = []

print(f'Digite "Sair" para finalizar o progama')
print('-'*70)

# Usando for para receber as vogais
for c in range(0, 5):
    vogais = str(input(f'Digite uma vogal: '))
    if (vogais != 'a' ) and (vogais != 'e') and (vogais != 'i') and (vogais != 'o') and (vogais != 'u'):
        break
    listadevogais.append(vogais)  
listadevogais.reverse()
print(f'A ordem inversa é: {listadevogais}')

     

    
    

    

    
        



