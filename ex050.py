'''
50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e
mostre na tela:
a) Quais foram os números sorteados
b) Quantos números estão acima de 5
c) Quantos números são divisíveis por 3
'''

import random

i = 0
qtd_numeros_maiores_cinco = 0
qtd_numeros_divisiveis_tres = 0
lista_numeros_aleatorios = []


while i < 20:
    numero_aleatorio = random.randint(1, 10)
    lista_numeros_aleatorios.append(numero_aleatorio)
    
    if numero_aleatorio > 5:
        qtd_numeros_maiores_cinco+=1

    if numero_aleatorio % 3 == 0:
        qtd_numeros_divisiveis_tres+=1

    i+=1

print(f'\nOs números sorteados foram: {lista_numeros_aleatorios}')
print(f'Quantidade de números maiores que 5: {qtd_numeros_maiores_cinco}')
print(f'Quantidade de números divisiveis por 3: {qtd_numeros_divisiveis_tres}\n')
