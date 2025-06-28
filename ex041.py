'''
Desenvolva um programa que mostre na tela a seguinte contagem:
100 95 90 85 80 ... 0 Acabou!
'''

numero = 100

while numero >= 0:
    print(numero, end=' ')
    numero-=5

print('Acabou!')