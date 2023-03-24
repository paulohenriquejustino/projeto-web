# Curso Técnico de Informática
# Autor: Ph
# Data: 04/12/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os

# Limmpando o terminal

os.system('cls')

# Declaração 

respotas = ' '
nome = 0
idade = 0
salario = 0 
sexo = 0
estadocivil = 0

# Entrada de dados
nome = str(input(f'Digite seu nome: '))
idade = int(input(f'Qual é sua idade: '))
salario = int(input(f'Digite seu sálario: '))
sexo = str(input(f'Qual é seu Sexo: ')).lower()
estadocivil = str(input(f'Seu estado civil é: '))



# Condicional

if(len(nome)<=3):
    print(f'Digite um nome com mais que 3 caracteres!')
else:
    if ( idade < 0 or idade > 150):
     print(f'Digite apenas idade entre 0 a 150!')
    else: 
     if(salario < 0):
      print(f'Digite um sálario maior que 0!')
     else:
        if ( sexo != 'f' and sexo != 'm'):
            print(f'Sexo apenas "f" ou "m"')
        else:
             if( sexo != 's' or sexo != 'c' or sexo != 'v' or sexo != 'd'):
            
               print(f'Estado civil valor apenas as letras "s", "c" "v" "d" ')
             else:
                print(f'Todos os campos corretos.')

              

         
        
        

         




        
       
 
      

    
   
  

