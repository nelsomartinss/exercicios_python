'''
Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1,
marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...
'''

numero = 30

while numero <= 30:
    if numero % 4 == 0:
        print(f'[{numero}]', end=' ')
    else:
        print(numero, end=' ')
    numero-=1

    if numero <= 0:
        break