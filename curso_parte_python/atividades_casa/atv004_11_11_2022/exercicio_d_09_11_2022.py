# Curso Técnico de Informática
# Autor: Ph
# Data: 12/11/2022

# Importanto as Blibliotecas

import os

# Limpando termninal

os.system('cls')

# Entrada


salario = float(input('Digite o sálario: '))

# Cálculos (condicional)

# No primeiro if faço o teste do verdadeiro, logo abaixo a soma do porcentual. 
# O uso do (/ 10) na linha 24, foi uma forma de resolver o erro de cálculo.

if ( salario > 1500):
    soma = salario * (0.5) / 100
    print(f'O percentual de aumento será de {soma:} porcento.')

# No else faz o teste do falso, acompanhado tambem com a soma do percentual.
    
else:
    (salario < 1000)    
    soma2 = salario * 0.10 / 100
    print(f'O percentual de aumento será de {soma2} porcento.')

