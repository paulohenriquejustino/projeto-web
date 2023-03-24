# Curso Técnico de Informática
# Autor: Ph
# Data: 18/11/2022
# Primeiro Progama em Python

# Importanto  as bibliotecas
import os
# Limmpando o terminal

os.system('cls')

from datetime import datetime
from datetime import date

# Declarando uma variavel data
data = datetime.now()

# Declarando uma variavel data formatada
data_formatada = data.strftime('%d/%m/%Y')

# Declarando um variavel data e hora formatada
data_hora_formatado = data.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatado}')

# Recebendo o ano
data_atual = data.today()
nascimento = 2003

# Imprimindo só o ano
print(f'Ano atual: {data_atual.year}')

idade = data_atual.year - nascimento


# Imprimindo só  a idade
print(f'Sua idade é: {idade} anos')


