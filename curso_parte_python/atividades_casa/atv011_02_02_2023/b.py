# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

# Declração
nomedoaluno = str
matricula =  int
anodenascimento = str
dados = []


# Criando funçoes
def cadastro():
    global nomedoaluno
    global matricula
    global anodenascimento
    global dados
    nomedoaluno = str(input(f'Digite o nome do aluno: '))
    matricula =  int(input(f'Digite o número da matricula: '))
    anodenascimento = str(input(f'Digite o ano de nascimento separados com /. '))

    
    for c in range(0, 1):    
        dados.append(nomedoaluno)
        dados.append(matricula)
        dados.append(anodenascimento)
        print(dados)

   
cadastro()


        







