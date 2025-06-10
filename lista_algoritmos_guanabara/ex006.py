'''
6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10
'''

numero = input('Digite um número: ')

int_numero = int(numero)
antecessor = int_numero - 1
sucessor = int_numero + 1

print(f'Número digitado: {int_numero}')
print(f'Antecessor: {antecessor}')
print(f'Sucessor: {sucessor}')