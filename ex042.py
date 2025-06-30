'''
42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
qualquer e mostre uma contagem até esse valor:
Ex: Digite um valor: 35
Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!
'''

numero = input('Digite um número: ')

try:
    int_numero = int(numero)
    numero_contador = 0

    while numero_contador <= int_numero:
        print(numero_contador, end=' ')
        numero_contador+=1
except:
    print('Você não digitou um número inteiro!')
    exit()

print('Acabou!')