'''
 Crie um programa que calcule e mostre na tela o resultado da soma entre 6 +
8 + 10 + 12 + 14 + ... + 98 + 100.
'''

contador = 6
somatorio = 0

while contador <= 100:
    somatorio+=contador
    contador+=2

print(f'A soma total é {somatorio}')