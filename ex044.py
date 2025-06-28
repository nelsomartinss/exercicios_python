'''
Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
incremento, mostrando em seguida todos os valores no intervalo:
Ex: Digite o primeiro Valor: 3
Digite o último Valor: 10
Digite o incremento: 2
Contagem: 3 5 7 9 Acabou!
'''

valor_inicial = input('Digite o valor inicial da contagem: ')
valor_final = input('Digite o valor final da contagem: ')
incremento = input('Digite o incremento: ')

try:
    inicio = int(valor_inicial)
    fim = int(valor_final)
    int_incremento = int(incremento)
except:
    print('Digite apenas números inteiros!')
    exit()

numero_contador = inicio

print('Contagem:', end=' ')

while numero_contador < fim:
    print(f'{numero_contador}', end=' ')
    numero_contador+=int_incremento

print('Acabou!')