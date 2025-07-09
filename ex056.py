'''
Crie um programa que leia vários números pelo teclado e mostre no final o
somatório entre eles.
Obs: O programa será interrompido quando o número 1111 for digitado
'''

somatorio = 0

while True:
    numeros = input('Digite um número: ')

    try:
        numeros = float(numeros)
    except:
        print('\nPor favor, digite apenas números!\n')
        continue

    somatorio+=numeros
    print(f'Somatorio de números: {somatorio :.1f}')

    if numeros == 1111:
        print('\nPrograma encerrado.\n')
        break