'''
[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
'''

import random

# NUMERO ALEATORIO
numero_sorteado = random.randint(1, 5)

# ENTRADAS
numero_adivinhado = input('Qual foi o número escolhido?\n')
int_numero_adivinhado = int(numero_adivinhado)

# PROCESSAMENTO
acertou = int_numero_adivinhado == numero_sorteado
errou = int_numero_adivinhado != numero_sorteado

# SAIDA
if acertou:
    print('ACERTOU')
elif errou:
    print(f'ERROU - O número era {numero_sorteado}')
