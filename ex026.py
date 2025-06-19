'''
26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
 - O primeiro valor é o maior
 - O segundo valor é o maior
 - Não existe valor maior, os dois são iguais
'''

primeiro_valor = input('Digite um número inteiro: ')
segundo_valor = input('Digite outro número inteiro: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'O primeiro valor é maior: {int_primeiro_valor}')
elif int_segundo_valor > int_primeiro_valor:
    print(f'O segundo valor é maior: {int_segundo_valor}')
else:
    print('Não existe valor maior, os dois são iguais')