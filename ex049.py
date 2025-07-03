'''
Crie um programa que leia 6 números inteiros e no final mostre quantos deles
são pares e quantos são ímpares.
'''

contador = 0
numeros_pares = 0
numeros_impares = 0

print('')
while contador < 6:
    numero = input('Digite um número inteiro: ')

    try:
        int_numero = int(numero)
    except ValueError:
        print('\nAlgo deu errado!\nDigite um número inteiro!\n')
        continue

    if int_numero % 2 == 0:
        numeros_pares+=1
    else:
        numeros_impares+=1
    
    contador+=1
    
print(f'\n{numeros_pares} números são PARES\n{numeros_impares} números são IMPARES\n')