''' 
4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório
entre eles.
Ex:
Digite um valor: 8
Digite outro valor: 5
A soma entre 8 e 5 é igual a 13. 
'''

primeiro_numero = input('Digite o primeiro número: ')
segundo_numero = input('Digite o segundo número: ')

int_primeiro_numero = int(primeiro_numero)
int_segundo_numero = int(segundo_numero)
soma = int_primeiro_numero + int_segundo_numero

print(f'{int_primeiro_numero} + {int_segundo_numero} = {soma}')
