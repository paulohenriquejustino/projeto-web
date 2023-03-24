# Curso Técnico de Informática
# Autor: Ph
# Data: 30/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')


# Declaraçao
n=1

# Usando while
while n<=100:
    mult=0
    for count in range(2,n):
        if (n % count == 0):
            mult += 1

    if(mult==0):
        print(n)
    n=n+2
       
   

        
    
       

   

