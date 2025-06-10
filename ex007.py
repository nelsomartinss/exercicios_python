'''
7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
sua terça parte.
Ex:
Digite um número: 3.5
O dobro de 3.5 é 7.0
A terça parte de 3.5 é 1.16666
'''

numero = input('Digite um número: ')

int_numero = int(numero)
dobro = int_numero * 2
terça_parte = int_numero / 3

print(f'Número digitado: {int_numero}')
print(f'Dobro: {dobro}')
print(f'Triplo: {terça_parte:.2f}')