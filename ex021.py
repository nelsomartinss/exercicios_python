'''
21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
BISSEXTO.
'''

ano = input('Digite um ANO: ')
int_ano = int(ano)

if (int_ano % 4 == 0 and int_ano % 100 != 0) or (int_ano % 400 == 0):
    print(f'{int_ano} é bissexto!')
else:
    print(f'{int_ano} NÃO é bissexto!')