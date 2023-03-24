from prettytable import PrettyTable
# Curso Técnico de Informática
# Autor: Ph
# Data: 02/02/2023

# Importanto  as bibliotecas
import os

# Limmpando o terminal
os.system('cls')

import random

# Definindo o número aleatório
numero = random.randint(0, 10)

# Definindo a pontuação máxima e mínima
pontuacao_maxima = 100
pontuacao_minima = 10

# Definindo o número máximo de tentativas
max_tentativas = 5

# Loop principal do jogo
tentativas = 0
while tentativas < max_tentativas:
    # Pedindo a entrada do usuário
    while True:
        try:
            palpite = int(input("Digite um número de 0 a 10: "))
            if palpite < 0 or palpite > 10:
                print("O número deve estar entre 0 e 10.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido.")
    
    # Verificando o palpite do usuário
    if palpite == numero:
        # Pontuação máxima se o usuário acertar na primeira tentativa
        if tentativas == 0:
            pontuacao = pontuacao_maxima
        else:
            # Pontuação diminui linearmente com o número de tentativas
            pontuacao = pontuacao_maxima - (tentativas * ((pontuacao_maxima - pontuacao_minima) / max_tentativas))
        print(f"Parabéns! Você acertou o número {numero} em {tentativas + 1} tentativas e marcou {pontuacao} pontos.")
        break
    else:
        print("Errou! Tente novamente.")
        tentativas += 1

# Se o usuário não acertar o número, não recebe pontuação
if tentativas == max_tentativas:
    print(f"Suas {max_tentativas} tentativas acabaram. O número era {numero}.")

