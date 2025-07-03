''' Faça um programa que leia 7 números inteiros e no final mostre o somatório
entre eles. '''

contador = 0
somando = 0

while contador < 7:
    numero = input('Digite um número inteiro: ')
    
    try:
        int_numero = int(numero)
    except ValueError:
        print('\nAlgo deu errado!\nDigite um número inteiro!\n')
        continue

    somando+=int_numero
    contador+=1

print(f'\nResultado da soma: {somando}\n')