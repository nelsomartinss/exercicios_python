'''
[DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de
agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
tentativas para tentar acertar.
'''
import random

numero_aleatorio = random.randint(1, 10)
numero_tentativas = 4
i = 1

print('')
while i <= 4:
    numero = input('Qual o número sorteado pelo computador (1 - 10)?\n')

    try:
        numero = int(numero)
    except:
        print('\nPor favor, digite um número inteiro...\n')

    if numero == numero_aleatorio and numero_tentativas != 4:
        print('\nYou Win!!\n')
        break
    else:
        print('\nTente novamente!')
        numero_tentativas-=1
        print(f'Tentativas restantes: {numero_tentativas}\n')

        if numero_tentativas == 0:
            print('\nGame Over!\n')
            break

        i+=1
        continue
    
