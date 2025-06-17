'''
20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
ÍMPAR.
'''

numero = input('Digite um número inteiro: ')
int_numero = int(numero)

if int_numero % 2 == 0:
    print(f'{int_numero} é PAR!')
else:
    print(f'{int_numero} é IMPAR!')